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

'''Function to check if user has visited an infected location in last 14 days and should isolate
Args: gRPC stub and variables to pass to server: user nric
Returns: dict of location and check-in datetime pairs'''
def check_cases(stub, nric):
    response = stub.CheckCases(safeentry_pb2.LocationCheck(nric=nric))

    locationDict = {}

    # Split the dict string into locations first
    # remove the last element because it's empty
    for i in response.locationList.split(";")[:-1]:
        location = i.split("|")
        locationDict[location[0]] = location[1]

    return locationDict

'''Function to add location to list of infected locations
Args: gRPC stub and variables to pass to server: location'''
def flag_location(stub, location, dateTime):
    response = stub.FlagLocation(safeentry_pb2.FlagRequest(location=location, datetime=dateTime))
    print(response.message)

########################
### PYTHON FUNCTIONS ###
########################

'''Function to get current datetime
Returns string with current date and time (e.g. 24/12/2018, 04:59:31)'''
def get_current_datetime():
    now = datetime.now()
    return now.strftime("%d/%m/%Y, %H:%M:%S")

'''Function to print alert to user when they visited infected location'''
def notify(dict):
    # visitedCases = check_cases(nric)
    
    if len(dict) > 0:
        print("Alert:")
        print("You have been in the same location as a Covid case:")

        #TODO maybe only get the latest location 
        for i in dict:
            print(f"{i} on {dict[i]}")

        print("Please isolate yourself until") #TODO


if __name__ == "__main__":
    # Establishing channels and stubs before every function incurs overhead
    # So establish once here and reuse
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = safeentry_pb2_grpc.SafeEntryStub(channel)

        # checkin(stub, "TJ", "S087896T", "SIT", get_current_datetime())

        # checkout(stub, "S087896T", get_current_datetime())

        notify(check_cases(stub, "S1"))

        # testgroup = ["S1", "S2"]
        # testnames = ["A", "B"]

        # checkin_group(stub, testnames, testgroup, "SIT", get_current_datetime())

        # checkout_group(stub, testgroup, get_current_datetime())

        # print(get_history(stub, "S3"))

        # now = datetime.now()
        # flag_location(stub, "Tekong", now.strftime("%d/%m/%Y, %H:%M:%S"))
