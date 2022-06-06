import grpc
import hello_pb2
import hello_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:12346') as channel:
        stub = hello_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(hello_pb2.HelloRequest(name="Emanuel"))
        print(f'response is : {response.response}')


if __name__ == "__main__":
    run()

