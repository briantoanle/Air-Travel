from Flight import *
from Airport import *

allAirports = []
allFlights = {}
def loadData(airportFile, flightFile):

    try:
        with open(airportFile,'r') as f:
            for line in f:
                l1 = line.split(',')
                for i in range(len(l1)):
                    l1[i] = l1[i].strip()
                #print(l1)
                airObject = Airport(l1[0],l1[2],l1[1])
                allAirports.append(airObject)
        #print(allAirports)
        airportList = []
        with open(flightFile, 'r') as t:
            for line in t:
                l2 = line.split(',')
                for i in range(len(l2)):
                    l2[i] = l2[i].strip()
                airportList.append(l2)

        for i in range(len(airportList)):
            flight = Flight(airportList[i][0],getAirportByCode(airportList[i][1]),getAirportByCode(airportList[i][2]))
            #print(airportList[i][0])
            #flightDict[]
            airportName = airportList[i][1]
            if airportName not in allFlights:
                flightList = [flight]
                allFlights[airportName] = flightList
                #print(flightList)
            else:
                allFlights[airportName].append(flight)
        #print(allFlights)
        # need flightNo, origin, destination
                # print(l2)

                # to create a flight you need 3 things:
                # 1. Flight number, you already have "XJ595

                # 2. Origin Airport, this you don't have
                # you only have the string name :)

                # 3. same as above

                # ---> then now, you have got a FLIGHT
                # make dictionary
                # key is the String Airport Code of the Origin Airport
                # if key is already exist in this dictionary
                # if not exist, create a new entry for this dictionary,
                # this entry contains: key as Origin Airport, value is an empty LIST of FLIGHT
                # then you add the first FLIGHT into this list

                # else, you know this entry is already in the dictionary
                # so you just get access directly to the LIST of FLIGHT, add the current FLIGHT to the list

            #airport1 = Airport(airportList[1])
            #flightObj = Flight(airportList[0],airportList[1],airportList[2])


        return True
    except FileNotFoundError:
        return False



def getAirportByCode(code):
    for ap in allAirports:
        # print(ap)
        if ap.getCode() == code:
            return ap

    return None

def findAllCityFlights(city):
    tempList = []
    for key, value in allFlights.items():
        for i in value:
            print(i.getOrigin().getCity())
            if i.getOrigin().getCity() == city or i.getDestination().getCity() == city:
                tempList.append(i)
    return tempList

def findAllCountry

def main():
    print("hello world")
    loadData('airports.txt', 'flights.txt')
    #airport1 = Airport("ATL", "Atlanta", "USA")
    #airport2 = Airport("EWR", "New Jersey", "USA")
    #print(airport1)
    #print(allAirports)
    # print(allFlights)
    #ai = getAirportByCode('ATL')
    #print("The object airport that I want to get is:", ai)
    #print(allFlights['ATL'])

    # for row in allFlights:
    #    for i in allFlights[row]:
    #        j=0






main()
