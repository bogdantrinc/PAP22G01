from concurrent import futures

import grpc
import hello_pb2
import hello_pb2_grpc


class Greater(hello_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return hello_pb2.HelloReplay(response=f"Yes {request.name}.")

    def GetData(self, request, context):
        return hello_pb2.GiveResponse(result=request.width*request.length)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
    hello_pb2_grpc.add_GreeterServicer_to_server(Greater(), server)
    server.add_insecure_port("[::]:12345")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
