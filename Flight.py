from Airport import *

class Flight:
    def __init__(self, flightNo, origin, destination):

        originCheck = isinstance(origin, Airport)
        destinationCheck = isinstance(destination, Airport)

        if originCheck == False or destinationCheck == False:
            raise TypeError('The origin and destination must be Airport objects')

        else:
            self._flightNo = flightNo
            self._origin = origin
            self._destination = destination

    def __repr__(self):
        domFlight = self.isDomesticFlight()
        if domFlight:
            return 'Flight: ' + self._flightNo + f' from {self._origin.getCity()} to {self._destination.getCity()}' + f' {{domestic}}'
        else:
            return 'Flight: ' + self._flightNo + f' from {self._origin.getCity()} to {self._destination.getCity()}' + f' {{international}}'

    def __eq__(self, other):
        # to be considered the same flight:
        # flight's origin and destination must be the same
        #print('origin',self.getOrigin() == other.getOrigin())
        #print('destination',self.getDestination() == other.getDestination())
        if self.getOrigin() == other.getOrigin() and self.getDestination() == other.getDestination():
            return True

        else:
            #print('eh')
            return False

    def getFlightNumber(self):
        return self._flightNo

    def getOrigin(self):
        return self._origin

    def getDestination(self):
        return self._destination

    def isDomesticFlight(self):
        return self._origin.getCountry() == self._destination.getCountry()


    def setOrigin(self,origin):
        self._origin = origin

    def setDestination(self,destination):
        self._destination = destination

#flight1 = Flight('XJX595',,'CPT')
#print(flight1.getFlightNumber())


def main():
    #print("hello world")
    airport1 = Airport("ATL", "Atlanta", "USA")
    airport2 = Airport("EWR", "New Jersey", "USA")
    flightA = Flight("ABC123", airport1, airport2)
    flightB = Flight('XJZ123',airport1,airport2)
   # print(flightA.getOrigin()==flightB.getOrigin())

    #print(flightA.getDestination()==flightB.getDestination())

    #  print(flightA == flightB)
main()
