import decimal


# Classes
class Airport:
    def __init__(self, IATACode, fullName, distanceFromLPL, distanceFromBOH):
        self.IATACode = str(IATACode).upper()
        self.fullName = str(fullName)
        self.distanceFromLPL = int(distanceFromLPL)
        self.distanceFromBOH = int(distanceFromBOH)

    def __str__(self):
        return f"## {self.fullName} ##\nIATA Code: {self.IATACode}\nDistance from LPL: {self.distanceFromLPL}\nDistance from BOH: {self.distanceFromBOH}"


class Plane:
    def __init__(self, planeType):
        self.planeType = planeType
        match planeType:
            case "Medium Narrow Body":
                self.runningCostPer100KM = decimal.Decimal(8)
                self.maxFlightRange = 2650
                self.allStandardCapacity = 180
                self.minFirstClassSeats = 8
            case "Large Narrow Body":
                self.runningCostPer100KM = decimal.Decimal(8)
                self.maxFlightRange = 5600
                self.allStandardCapacity = 220
                self.minFirstClassSeats = 10
            case "Medium Wide Body":
                self.runningCostPer100KM = decimal.Decimal(5)
                self.maxFlightRange = 4050
                self.allStandardCapacity = 406
                self.minFirstClassSeats = 14
    def __str__(self):
        return f"## Plane ##\nPlane Type: {self.planeType}\nRunning Cost/100km: {self.runningCostPer100KM}\nMax Flight Range: {self.maxFlightRange}\nCapacity If All Seats Are Standard: {self.allStandardCapacity}\nMinimum Number of First-Class Seats (if any): {self.minFirstClassSeats}"



class Flight:
    def __init__(self):
        self.UKAirport = "LPL"
        self.overseasAirport = Airport("NON", "NONE", 0, 0)
        self.distance = self.overseasAirport.distanceFromLPL if self.UKAirport == "LPL" else self.overseasAirport.distanceFromBOH
        self.plane = Plane("Medium Narrow Body")
        self.firstClassSeats = 0
        self.standardClassSeats = 220 - self.firstClassSeats
        self.standardSeatPrice = 0
        self.firstClassSeatPrice = decimal.Decimal(0)
        self.perSeatFlightCost = decimal.Decimal(0)
        self.totalFlightCost = decimal.Decimal(0)
        self.flightIncome = decimal.Decimal(0)
        self.flightProfit = decimal.Decimal(0)
    def __str__(self):
        return f"## Flight ##\nFrom: {self.UKAirport}\nTo: {self.overseasAirport.IATACode}\nDistance: {self.distance}\n# Plane #\nPlane Type: {self.plane.planeType}\nMaximum Flight Range: {self.plane.maxFlightRange}\nRunning Cost/Seat/100km: {self.plane.runningCostPer100KM}\nCapacity If All Seats Are Standard: {self.plane.allStandardCapacity}\nStandard Class Seats: {self.standardClassSeats}\nStandard Class Seat Price: {self.standardSeatPrice}\nFirst Class Seats: {self.firstClassSeats}\nFirst Class Seat Price: {self.firstClassSeatPrice}\n# Income #\nFlight Cost Per Seat: {self.perSeatFlightCost}\nTotal Cost of Flight: {self.totalFlightCost}\nFlight Income: {self.flightIncome}\nFlight Profit: {self.flightProfit}"
    # TODO Add:
    # TODO cost per seat, total cost, income, profit
    



def main():
    pass

def classTests():
    a = Airport("DIK", "BALLS", 420, 69)
    p = Plane("Medium Wide Body")
    f = Flight()
    f.UKAirport = "LPL"
    f.overseasAirport = a
    f.plane = p
    f.firstClassSeats = 20
    print(a)
    print("\n")
    print(p)
    print("\n")
    print(f)

# if __name__ == "__main__":
#     """Entry point of program"""
#     main()
classTests()