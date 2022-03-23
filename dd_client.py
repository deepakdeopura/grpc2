import grpc
import dd_grps_sample_pb2_grpc as pb2_grpc
import dd_grps_sample_pb2 as pb2



class ddClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

       
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.ddgreetingStub(self.channel)

    def get_url(self, message):

        message = pb2.Message(message=message)
        print(f'{message}')
        return self.stub.GetServerResponse(message)


if __name__ == '__main__':
    client = ddClient()
    result = client.get_url(message="Hello GRPC server")
    print(f'{result}')