# from asyncio.windows_events import NULL
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

        if nric in self.data_file:
            print('NRIC already exist')
            cur = self.data_file[nric]

            #temporary store key and values
            new_location = {
                "location": location,
                "checkInDateTime": dateTime,
                "checkOutDateTime": ""
            }

            cur.append(new_location)

        else:
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

        selected_user[-1]["checkOutDateTime"] = dateTime
        print(selected_user[-1]["checkOutDateTime"])

        json_obj = json.dumps(self.data_file, indent=4)

        with open("datas/datas.json", "w") as out:
            out.write(json_obj)

            

    def addLocation(self, location, dateTime):

        #dateTime input comes in only with date
        dateTime += ", 00:00:00"

        location = {
            location:
                {
                    "Date": dateTime
                }
        }

        self.location_file.update(location)

        json_obj = json.dumps(self.location_file, indent=4)

        with open("datas/location.json", "w") as out:
            out.write(json_obj)

    '''Function to get list of locations visited by a Covid case within past 14 days
    Returns list of locations'''

    def getLocation(self):
        locationList = {}

        ## 2022/6/4
        now = datetime.now()
        cur = now - timedelta(days=14)

        for i in self.location_file:
            locationDate = self.location_file[i]["Date"]
            locationDateParsed = datetime.strptime(locationDate, '%d/%m/%Y, %H:%M:%S')

            #If date visited by Covid case is within 14 days before current date
            if (locationDateParsed > cur):
                locationList[i] = locationDate

        print("Infected locations:", locationList)

        return locationList

    '''Function to get list of locations visited by user
    Returns list of locations'''

    def getVisited(self, nric):
        locationList = []

        if not self.nricExists(nric):
            return locationList

        for i in self.data_file[nric]:
            locationList.append(i["location"])

        print(locationList)

        return locationList

    '''Function to check if user has visited an infected location within past 14 days
    Args: nric of user and list of infected locations
    Returns dict of location and vist datetime pairs, in the form of a string
    Couldn't successfully send dicts over gRPC'''

    def getCases(self, nric, infectedLocation: list) -> str:
        locationDict = ""

        if not self.nricExists(nric):
            return locationDict

        now = datetime.now()
        cur = now - timedelta(days=14)

        visitedLocation = self.data_file[nric]
        # print(visitedLocation)
        for j in visitedLocation:
            locations = j["location"]
            locationDateTime = j["checkInDateTime"]
            locationDateTimeParsed = datetime.strptime(locationDateTime, '%d/%m/%Y, %H:%M:%S')
            
            # If user visited before infection, shouldn't notify
            if locationDateTimeParsed > cur and locations in infectedLocation:

                infectedDateTimeParsed = datetime.strptime(infectedLocation[locations], '%d/%m/%Y, %H:%M:%S')
                if locationDateTimeParsed > infectedDateTimeParsed: 
                    locationDict += f"{locations}|{locationDateTime};"

        print(f"Infected locations visited by {nric}: '{locationDict}'")
        return locationDict

    '''Reusable function to check if NRIC exists in datas.json
    Returns true if so'''

    def nricExists(self, nric):
        if nric in self.data_file:
            return True
        else:
            return False
