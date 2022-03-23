import grpc
from concurrent import futures
import time
import dd_grps_sample_pb2_grpc as pb2_grpc
import dd_grps_sample_pb2 as pb2


class ddgreetingService(pb2_grpc.ddgreeting):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):

        # get the string from the incoming request
        message = request.message
        result = f'Hello  GRPC Client ,I am GRPC server up and running received "{message}" message from you'
        result = {'message': result, 'received': True}

        return pb2.MessageResponse(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ddgreetingServicer_to_server(ddgreetingService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()