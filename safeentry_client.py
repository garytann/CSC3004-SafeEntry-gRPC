from datetime import datetime

import grpc
import safeentry_pb2
import safeentry_pb2_grpc

# To build gRPC stubs:
# python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/safeentry.proto

### GRPC Functions ###

'''Function to log a checkin to server
Args: gRPC stub and variables to pass to server: user name, NRIC, building name, checkin datetime'''


def checkin(stub, name, nric, location, checkin):
    response = stub.CheckIn(safeentry_pb2.CheckInRequest(name=name, nric=nric, location=location, checkin=checkin))
    print(response.message)


'''Function to log a checkout from existing location to server
Checkout doesn't need name, just needs NRIC to find user in database
Args: gRPC stub and variables to pass to server: NRIC, checkout datetime'''


def checkout(stub, nric, checkout):
    response = stub.CheckOut(safeentry_pb2.CheckOutRequest(nric=nric, checkout=checkout))
    print(response.message)


'''Function to checkin a group of people
Args: gRPC stub and variables to pass to server: list of names, list of NRICs, location and checkin datetime'''


def checkin_group(stub, nameList: list, nricList: list, location, checkin):
    # List inputs must be list
    # If the input is only a single string input ("Dave" instead of ["Dave"]), 
    # the server would split the string into multiple characters and think they are individual people (["D", "A", "V", "E"])
    if type(nameList) != list or type(nricList) != list:
        print("Failure")
        print("Input must be lists")
        return

    # Also check if there are more ICs or names than the other
    if len(nameList) != len(nricList):
        print("Failure")
        print("Number of names and NRIC do not match")
        return

    response = stub.CheckInGroup(
        safeentry_pb2.GroupInRequest(name=nameList, nric=nricList, location=location, checkin=checkin))
    print(response.message)


'''Function to checkout a group of people
Args: gRPC stub and variables to pass to server: list of NRICs and checkout datetime'''


def checkout_group(stub, nricList: list, checkout):
    if type(nricList) != list:
        print("Failure")
        print("Input must be a list")
        return

    response = stub.CheckOutGroup(safeentry_pb2.GroupOutRequest(nric=nricList, checkout=checkout))
    print(response.message)


'''Function to get list of visited locations
Args: gRPC stub and variables to pass to server: nric'''


def get_history(stub, nric):
    response = stub.LocationHistory(safeentry_pb2.HistoryRequest(nric=nric))

    for location in response.locations:
        print(location)


'''Function to check for positive covid cases
Requirement: within the past 14 days
'''


def check_cases(stub,nric):
    response = stub.CheckCases(safeentry_pb2.LocationCheck(nric=nric))
    print(response)


########################
### PYTHON FUNCTIONS ###
########################

'''Function to get current datetime
Returns string with current date and time (e.g. 24/12/2018, 04:59:31)'''


def get_current_datetime():
    now = datetime.now()
    return now.strftime("%d/%m/%Y, %H:%M:%S")


if __name__ == "__main__":
    # Establishing channels and stubs before every function incurs overhead
    # So establish once here and reuse
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = safeentry_pb2_grpc.SafeEntryStub(channel)

        # checkin(stub, "TJ", "S087896T", "SIT", get_current_datetime())

        # checkout(stub, "S087896T", get_current_datetime())

        check_cases(stub, "S087896T")

        testgroup = ["S1", "S2"]
        testnames = ["A", "B"]

        # checkin_group(stub, "A", "S1", "SIT", get_current_datetime())

        # checkout_group(stub, ["S1"], get_current_datetime())

        get_history(stub, "S1")
