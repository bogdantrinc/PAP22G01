import grpc
import hello_pb2
import hello_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:12345') as channel:
        stub = hello_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(hello_pb2.HelloRequest(name="Bogdan"))
        print(f'response is : {response.response}')
        result = stub.GetData(hello_pb2.GetMeasurements(width=2, length=2))
        print(f'Result is : {result.result}')


if __name__ == "__main__":
    run()

