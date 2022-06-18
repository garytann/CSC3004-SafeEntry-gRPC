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
    #TODO Ensure IC is 9 digits and starts with 'S' or 'T' and ends with letter
    def CheckIn(self, request, context):
        print(request.nric, request.location)
        #TODO Add name as well into JSON
        addData(request.nric, request.location, request.checkin)
        return safeentry_pb2.CheckInOutReply(message="Success")

    '''Function to take user checkin info
    Returns a CheckOutReply with success or failure'''
    def CheckOut(self, request, context):
        print(request.nric, request.checkout)
        updateData(request.nric, request.checkout)
        return safeentry_pb2.CheckInOutReply(message="Success")

    '''Function to take checkin info of groups
    Returns a CheckInReply with success or failure'''
    def CheckInGroup(self, request, context):
        #request.nric and request.name are lists
        for ic in request.nric:
            print(ic)
        return safeentry_pb2.CheckInOutReply(message="Success")

    '''Function to checkout groups
    Returns a CheckOutReply with success or failure'''
    def CheckOutGroup(self, request, context):
        #request.nric is a list
        for ic in request.nric:
            print(ic)
        return safeentry_pb2.CheckInOutReply(message="Success")

    '''Function to return list of locations visited
    Using user's NRIC, traverse through JSON db and collate all locations
    Returns list of locations'''
    def LocationHistory(self, request, context):
        #TODO JSON logic to find locations
        #TODO Check if NRIC exists
        locations = ["SP", "NYP", "Tekong"]
        return safeentry_pb2.HistoryReply(locations=locations)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    safeentry_pb2_grpc.add_SafeEntryServicer_to_server(SafeEntry(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

######################
### JSON FUNCTIONS ###
######################

def addData(nric, location, dateTime):
    with open("datas/datas.json", "r") as f:
        file = json.load(f)

    datas = {
        nric: [
            {
                "location": location,
                "checkInDateTime": dateTime,
                "checkOutDateTime": ""
            }
        ]
    }

    file.update(datas)

    json_obj = json.dumps(file, indent=4)

    with open("datas/datas.json", "w") as out:
        out.write(json_obj)

#TODO remember the last location checkedin to check out from
def updateData(nric, dateTime):
    with open("datas/datas.json", "r") as f:
        file = json.load(f)
    cur = file[nric]
    cur[0]["checkOutDateTime"] = dateTime
    print(cur[0]["checkOutDateTime"])

    json_obj = json.dumps(file, indent=4)

    with open("datas/datas.json", "w") as out:
        out.write(json_obj)

##TODO check if the location has covid in the past 14 days
def checkCases(nric, location):
    with open("datas/location.json", "r") as f:
        locations = json.load(f)



if __name__ == '__main__':
    logging.basicConfig()
    serve()
