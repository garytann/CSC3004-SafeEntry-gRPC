from datetime import datetime, timedelta

import grpc
from time import sleep
import safeentry_pb2
import safeentry_pb2_grpc

# To build gRPC stubs:
# python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/safeentry.proto


### THIS IS A TEST SCRIPT THAT AUTORUNS FUNCTIONS ###
#####################################################


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

    #TODO test when locationdict is empty

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

    if len(dict) > 0:
        print("\nAlert:")
        print("You have been in the same location as a Covid case:")

        oldest_date = datetime.now() - timedelta(days=14)
        key = ""
        
        # Only get infected location that was visited most recently
        for i in dict:
            loc_date = datetime.strptime(dict[i], '%d/%m/%Y, %H:%M:%S')
            if loc_date > oldest_date:
                oldest_date = loc_date
                key = i

        print(f"{key} on {dict[key]}")

        print("Please isolate yourself for 14 days until:\n") 
        print(datetime.strftime(oldest_date + timedelta(days=14), '%d/%m/%Y, %H:%M:%S'))

    else:
        print("\nYou are safe from Covid")
        print("Let's keep it that way\n")


if __name__ == "__main__":
    # Establishing channels and stubs before every function incurs overhead
    # So establish once here and reuse
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = safeentry_pb2_grpc.SafeEntryStub(channel)

        #Test variables
        nric = "S1234567A"
        name = "TEST1"
        loc = "Takashimaya"

        print("Welcome to PrettySafeEntry")
        print("\nPlease enter a valid NRIC: ", end="")
        sleep(2)
        print(nric)

        notify(check_cases(stub, nric)) # Check close contact status
        print(f"\nWelcome {name}, {nric}")

        print("Actions:")
        # For MOH staff
        if (nric=="admin"):
            print("0) Add infected location")
        print("1) Check-in to location")
        print("2) Check-out from previous location")
        print("3) Check-in group")
        print("4) Check-out group")
        print("5) Get visit history")
        print("Input choice (anything else to exit): ", end="")

        sleep(2)
        print("1")
        print()

        print("Input location: ", end="")
        sleep(2)
        print(loc)
        checkin(stub, name, nric, loc, get_current_datetime())
        print()

        print("Actions:")
        # For MOH staff
        if (nric=="admin"):
            print("0) Add infected location")
        print("1) Check-in to location")
        print("2) Check-out from previous location")
        print("3) Check-in group")
        print("4) Check-out group")
        print("5) Get visit history")
        print("Input choice (anything else to exit): ", end="")

        sleep(2)
        print("2")
        print()
        checkout(stub, nric, get_current_datetime())
        print()

        print("Actions:")
        # For MOH staff
        if (nric=="admin"):
            print("0) Add infected location")
        print("1) Check-in to location")
        print("2) Check-out from previous location")
        print("3) Check-in group")
        print("4) Check-out group")
        print("5) Get visit history")
        print("Input choice (anything else to exit): ", end="")

        sleep(2)
        print("5")
        print()
        print("\nPlaces checked-in:")
        get_history(stub, nric)
        print()

        print("TEST END")

        # # IC error checking loop
        # while True: 

        #     nric = input("\nPlease enter a valid NRIC:")

        #     if (len(nric) == 9 and (nric[0].upper() == 'S' or nric[0].upper() == 'T') 
        #     and nric[-1].isalpha() and nric[1:-2].isnumeric()) or nric=='admin':
        #         break

        #     if len(nric) != 9 :
        #         print("Incorrect NRIC length!")
        #     else:
        #         if nric[0].upper() != 'S' and nric[0].upper() != 'T':
        #             print("NRIC should start with S or T")
        #         if not nric[-1].isalpha():
        #             print("NRIC should end with a letter")
        #         if not nric[1:-2].isnumeric():
        #             print("NRIC needs 7 numbers")

        # if nric != 'admin':
        #     name = input("Input name: ")

        #     notify(check_cases(stub, nric)) # Check close contact status
        #     print(f"\nWelcome {name}, {nric}")
        # else:
        #     print("\nAdmin mode\n")

        # # Action loop
        # while True:
        #     print("Actions:")

        #     # For MOH staff
        #     if (nric=="admin"):
        #         print("0) Add infected location")
        #     print("1) Check-in to location")
        #     print("2) Check-out from previous location")
        #     print("3) Check-in group")
        #     print("4) Check-out group")
        #     print("5) Get visit history")

        #     choice = input("Input choice (anything else to exit): ")

        #     print()

        #     if choice.isalpha():
        #         break 
            
        #     # Choice
        #     if int(choice) == 0 and nric=='admin': 
        #             location = input("Input location: ")
        #             date = input("Input date in dd/mm/yyyy format: ")
        #             flag_location(stub, location, date)

        #     elif int(choice) == 1:
        #         location = input("Input location: ")
        #         checkin(stub, name, nric, location, get_current_datetime())

        #     elif int(choice) == 2:
        #         checkout(stub, nric, get_current_datetime())

        #     elif int(choice) == 3:
        #         names = []
        #         ics = []

        #         n = input("Number of people: ")

        #         while not n.isnumeric():
        #             print("Please input a number")
        #             n = input("Number of people: ")

        #         for i in range(int(n)):
        #             names.append(input(f"Input name of member {i+1}: "))
        #             ics.append(input(f"Input NRIC of member {i+1}: "))

        #         location = input("Input location: ")
        #         checkin_group(stub, names, ics, location, get_current_datetime())

        #     elif int(choice) == 4:
        #         ics = []

        #         n = input("Number of people: ")

        #         while not n.isnumeric():
        #             print("Please input a number")
        #             n = input("Number of people: ")

        #         for i in range(int(n)):
        #             ics.append(input(f"Input NRIC of member {i+1}"))

        #         checkout_group(stub, ics, get_current_datetime())

        #     elif int(choice) == 5:
        #         print("\nPlaces checked-in:")
        #         get_history(stub, nric)
            
        #     else:
        #         break

        #     print()

