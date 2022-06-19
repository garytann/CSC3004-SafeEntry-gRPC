from asyncio.windows_events import NULL
import json
from datetime import timedelta, datetime

class Database():
    
    '''Read and open json file first for optimised performance'''
    def __init__(self):
        self.data_file = json.load(open("datas/datas.json", "r"))
        self.location_file = json.load(open("datas/location.json", "r"))

    '''Function to add new SafeEntry data into datas.json
    Args: user's name, nric, visiting location and check in datetime'''
    def addData(self, name, nric, location, dateTime):
        datas = {
            nric: [
                {
                    "name": name,
                    "location": location,
                    "checkInDateTime": dateTime,
                    "checkOutDateTime": ""
                }
            ]
        }

        self.data_file.update(datas)

        json_obj = json.dumps(self.data_file, indent=4)

        with open("datas/datas.json", "w") as out:
            out.write(json_obj)

    '''Function to update existing SafeEntry entry with check out datetime
    Args: user's nric and check out datetime'''
    def updateData(self, nric, dateTime):
        selected_user = self.data_file[nric]

        # TODO remember the last location checkedin to check out from
        selected_user[0]["checkOutDateTime"] = dateTime
        print(selected_user[0]["checkOutDateTime"])

        json_obj = json.dumps(self.data_file, indent=4)

        with open("datas/datas.json", "w") as out:
            out.write(json_obj)


    '''Function to get list of locations visited by a Covid case within past 14 days
    Returns list of locations'''
    def getLocation(self):
        locationList = []
        
        ## 2022/6/4
        now = datetime.now()
        cur = now - timedelta(days=14)

        for i in self.location_file:
            locationDate = self.location_file[i]["Date"]
            locationDate = datetime.strptime(locationDate, '%d/%m/%Y')

            if (locationDate > cur):
                locationList.append(i)

        print(locationList)

        return locationList

    '''Function to check if user has visited an infected location within past 14 days
    Args: nric of user and list of infected locations
    Returns TODO'''
    def getCases(self, nric, infectedLocation: list):
        LocationList = []

        now = datetime.now()
        cur = now - timedelta(days=14)
      
        visitedLocation = self.data_file[nric]
        # print(visitedLocation)
        for j in visitedLocation:
            locations = j["location"]
            locationDateTime = j["checkInDateTime"]
            locationDateTime = datetime.strptime(locationDateTime, '%d/%m/%Y, %H:%M:%S')

            if locationDateTime > cur and locations in infectedLocation:
                locationDateTime = datetime.strftime(locationDateTime, '%d/%m/%Y, %H:%M:%S')
                LocationList.append(locations)
                LocationList.append(locationDateTime)
            # TODO add the nric and locations into a key value pair?

        print(LocationList)
        return LocationList