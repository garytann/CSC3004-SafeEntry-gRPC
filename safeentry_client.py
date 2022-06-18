from datetime import datetime

import grpc
import safeentry_pb2
import safeentry_pb2_grpc

'''Function to log a checkin to server
Args: gRPC stub and variables to pass to server: NRIC, building name, checkin datetime
Returns: Success/Failure message'''
def checkin(stub, nric, location, checkin):

    response = stub.CheckIn(safeentry_pb2.CheckInRequest(nric=nric, location=location, checkin=checkin))
    print(response.message)

'''Function to log a checkout from existing location to server
Args: gRPC stub and variables to pass to server: NRIC, checkout datetime
Returns: Success/Failure message'''
def checkout(stub, nric, checkout):
      
    response = stub.CheckOut(safeentry_pb2.CheckOutRequest(nric=nric, checkout=checkout))
    print(response.message)

# def checkin_group(stub, ):
    
#     response = stub.CheckIn(safeentry_pb2.CheckInRequest(nric=nric, location=location, checkin=checkin))
#     print(response.message)

if __name__ == "__main__":


    #Establishing channels and stubs before every function incurs overhead
    #So establish once here and reuse
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = safeentry_pb2_grpc.SafeEntryStub(channel)

        now = datetime.now()
        checkin(stub, "S087896T", "SIT", now.strftime("%H:%M:%S"))

        now = datetime.now()
        checkout(stub, "S1234567A", now.strftime("%H:%M:%S"))
