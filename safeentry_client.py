from datetime import datetime

import grpc
import safeentry_pb2
import safeentry_pb2_grpc

'''Function to log a checkin to server
Args: NRIC, building name, checkin datetime
Returns: Success/Failure message'''
def checkin(nric, location, checkin):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = safeentry_pb2_grpc.SafeEntryStub(channel)
        
        response = stub.CheckIn(safeentry_pb2.CheckInRequest(nric=nric, location=location, checkin=checkin))
        print(response.message)

'''Function to log a checkout from existing location to server
Args: NRIC, checkout datetime
Returns: Success/Failure message'''
def checkout(nric, checkout):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = safeentry_pb2_grpc.SafeEntryStub(channel)
        
        response = stub.CheckOut(safeentry_pb2.CheckOutRequest(nric=nric, checkout=checkout))
        print(response.message)

if __name__ == "__main__":
    now = datetime.now()
    checkin("S1234567A", "NYP", now.strftime("%H:%M:%S"))

    now = datetime.now()
    checkout("S1234567A", now.strftime("%H:%M:%S"))