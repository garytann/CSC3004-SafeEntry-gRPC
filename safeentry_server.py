from concurrent import futures
import logging

import grpc
import safeentry_pb2
import safeentry_pb2_grpc


class SafeEntry(safeentry_pb2_grpc.SafeEntryServicer):

    def CheckIn(self, request, context):
        return safeentry_pb2.CheckInReply(message="Success")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    safeentry_pb2_grpc.add_SafeEntryServicer_to_server(SafeEntry(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()