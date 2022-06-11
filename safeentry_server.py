from concurrent import futures
import logging

import grpc
import safeentry_pb2
import safeentry_pb2_grpc


class SafeEntry(safeentry_pb2_grpc.SafeEntryServicer):

    '''Function to take user checkin info
    Returns a CheckInReply with success or failure'''
    def CheckIn(self, request, context):
        print(request.nric, request.location)
        return safeentry_pb2.CheckInReply(message="Success")

    '''Function to take user checkin info
    Returns a CheckInReply with success or failure'''
    def CheckOut(self, request, context):
        print(request.nric)
        return safeentry_pb2.CheckOutReply(message="Success")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    safeentry_pb2_grpc.add_SafeEntryServicer_to_server(SafeEntry(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()