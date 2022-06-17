from concurrent import futures
import logging

import grpc
import safeentry_pb2
import safeentry_pb2_grpc
import json
from datetime import datetime


class SafeEntry(safeentry_pb2_grpc.SafeEntryServicer):
    '''Function to take user checkin info
    Returns a CheckInReply with success or failure'''

    def CheckIn(self, request, context):
        print(request.nric, request.location)
        addData(request.nric, request.location, request.checkin)
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


def addData(nric, location, dateTime):

    with open("datas/datas.json", "r") as f:
        file = json.load(f)

    datas = {
        nric: [
            {
                "location": location,
                "checkInDateTime": dateTime
            }
        ]
    }

    file.update(datas)

    with open("datas/datas.json", "w") as out:
        json.dump(file, out)

if __name__ == '__main__':
    logging.basicConfig()
    serve()
