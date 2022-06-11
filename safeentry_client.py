from datetime import datetime

import grpc
import safeentry_pb2
import safeentry_pb2_grpc

def checkin():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = safeentry_pb2_grpc.SafeEntryStub(channel)
        
        now = datetime.now()
        response = stub.CheckIn(safeentry_pb2.CheckInRequest(nric="S1234567A", location="NYP", checkin=now.strftime("%H:%M:%S")))
        print(response.message)


if __name__ == "__main__":
    checkin()