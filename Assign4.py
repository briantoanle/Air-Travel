from Flight import *
from Airport import *

allAirports = []
allFlights = {}


def loadData(airportFile, flightFile):

    try:
        with open(airportFile, 'r') as f:
            for line in f:
                l1 = line.split(',')
                for i in range(len(l1)):
                    l1[i] = l1[i].strip()

                airObject = Airport(l1[0], l1[2], l1[1])
                allAirports.append(airObject)

        airportList = []

        with open(flightFile, 'r') as t:
            for line in t:
                l2 = line.split(',')
                for i in range(len(l2)):
                    l2[i] = l2[i].strip()
                airportList.append(l2)


        for i in range(len(airportList)):

            flight = Flight(airportList[i][0], getAirportByCode(airportList[i][1]), getAirportByCode(airportList[i][2]))

            airportName = airportList[i][1]

            if airportName not in allFlights:
                flightList = [flight]
                allFlights[airportName] = flightList
            else:

                allFlights[airportName].append(flight)


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

        # airport1 = Airport(airportList[1])
        # flightObj = Flight(airportList[0],airportList[1],airportList[2])

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
            # print(i.getOrigin().getCity())
            if i.getOrigin().getCity() == city or i.getDestination().getCity() == city:
                tempList.append(i)

    return tempList


# lelele
def findAllCountryFlights(country):
    tempList = []
    for key, value in allFlights.items():
        for i in value:

            if i.getOrigin().getCountry() == country or i.getDestination().getCountry() == country:
                tempList.append(i)
    return tempList


def findFlightBetween(origAirport, destAirport):

    for key, value in allFlights.items():

        for i in value:
            #print(i)

            if i.getOrigin() == origAirport and i.getDestination() == destAirport:
                # print(origAirport,destAirport)
                return 'Direct Flight: ' + str(origAirport.getCode()) + ' to ' + str(destAirport.getCode())
    nl = []
    transitSet = set()
    for key, value in allFlights.items():

        for i in value:

            if i.getOrigin() == origAirport:

                transit = i.getDestination()
                nl.append(transit)
                #`print(transit)

        for i in nl:
            anotherValue = allFlights[i.getCode()]
            for j in anotherValue:

                if i == j.getOrigin() and j.getDestination() == destAirport:

                    #print(i.getCode())
                    transitSet.add(i.getCode())


    if len(transitSet) > 0:
        return transitSet
    else:
        return -1




def findReturnFlight(firstFlight):
    #print(firstFlight)
    #print(firstFlight.getOrigin())
    for key, value in allFlights.items():
        for i in value:
            if firstFlight.getDestination() == i.getOrigin() and firstFlight.getOrigin() == i.getDestination():
                return i

    else:
        return -1
'''
def main():
    #print("hello world")
    loadData('airports.txt', 'flights.txt')


    # airport1 = Airport("ATL", "Atlanta", "USA")
    # airport2 = Airport("EWR", "New Jersey", "USA")
    # print(airport1)
    # print(allAirports)
    # print(allFlights)
    # ai = getAirportByCode('ATL')
    # print("The object airport that I want to get is:", ai)
    # print(allFlights['ATL'])

    # for row in allFlights:
    #    for i in allFlights[row]:
    #        j=0
    # print(findAllCountryFlights('United States'))
    #print(findFlightBetween(getAirportByCode("YYZ"), getAirportByCode("CDG")))
    #print(getAirportByCode('PVG'))
    #print(getAirportByCode('DXB'))
    #print(findFlightBetween(getAirportByCode("PVG"), getAirportByCode("DXB")))
    #print(allFlights['PVG'])
    #for f in allFlights['PVG']:
        #print(f)
    #for f in allFlights['ICN']:
        #print(f)
    # findReturnFlight(
    #print(findFlightBetween(getAirportByCode("PVG"), getAirportByCode("DXB")))
    print(findReturnFlight(allFlights["BOG"][1]))
main()
'''
