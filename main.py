import decimal
import sys


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
    self.distance = 0
    self.plane = Plane("Medium Narrow Body")
    self.firstClassSeats = 0
    self.standardClassSeats = self.plane.allStandardCapacity - self.firstClassSeats
    self.standardSeatPrice = 0
    self.firstClassSeatPrice = decimal.Decimal(0)
    self.perSeatFlightCost = decimal.Decimal(0)
    self.totalFlightCost = decimal.Decimal(0)
    self.flightIncome = decimal.Decimal(0)
    self.flightProfit = decimal.Decimal(0)


  def setDistance(self):
    self.distance = self.overseasAirport.distanceFromLPL if self.UKAirport == "LPL" else self.overseasAirport.distanceFromBOH

  def setStandardClassSeats(self):
    self.standardClassSeats = self.plane.allStandardCapacity - self.firstClassSeats
  
  
  def __str__(self):
    return f"## Flight ##\nFrom: {self.UKAirport}\nTo: {self.overseasAirport.IATACode}\nDistance: {self.distance}\n# Plane #\nPlane Type: {self.plane.planeType}\nMaximum Flight Range: {self.plane.maxFlightRange}\nRunning Cost/Seat/100km: {self.plane.runningCostPer100KM}\nCapacity If All Seats Are Standard: {self.plane.allStandardCapacity}\nStandard Class Seats: {self.standardClassSeats}\nStandard Class Seat Price: {self.standardSeatPrice}\nFirst Class Seats: {self.firstClassSeats}\nFirst Class Seat Price: {self.firstClassSeatPrice}\n# Income #\nFlight Cost Per Seat: {self.perSeatFlightCost}\nTotal Cost of Flight: {self.totalFlightCost}\nFlight Income: {self.flightIncome}\nFlight Profit: {self.flightProfit}"


def main():
  airports = readAirportData("Airports.txt")
  newFlight = Flight()
  print(newFlight)
  mainMenu(airports, newFlight)

def readAirportData(fileName):
  airports = {}
  with open(fileName) as file:
    for line in file:
      newAirportAsList = str(line).split(",")
      newAirport = Airport(*newAirportAsList)
      airports[newAirport.IATACode] = newAirport
  return(airports)


def mainMenu(airports, newFlight):
  choiceOfAction = input("########## Main Menu ##########\nEnter a number to select the desired action.\n1 - Enter Airport Details\n2 - Enter Flight Details\n3 - Enter Price Plan and Calculate Potential Profit\n4 - Clear All Entered Data\n5 - Quit Program\n")
  match choiceOfAction:
    case "1":
      newFlight = enterAirportDetails(airports, newFlight)
      mainMenu(airports, newFlight)
    case "2":
      newFlight = enterFlightDetails(newFlight)
      mainMenu(airports, newFlight)
    case "3":
      enterPricePlanAndCalculateProfit(newFlight)
    case "4":
      clearData(airports, newFlight)
    case "5":
      print("Thank you for using the program. Goodbye.\n")
      sys.exit()
    case "X":
      print("Hello world")
      mainMenu(airports, newFlight)
    case _:
      print("Invalid choice of action.\n\n")
      mainMenu(airports, newFlight)

def enterAirportDetails(airports, newFlight):
  selectedAirport = input("Please enter the IATA code of the destination airport.").upper()
  if len(selectedAirport) > 3:
    print("Invalid IATA code.")
  else:
    try:
      newFlight.overseasAirport = airports[selectedAirport]
    except Exception:
      print("This airport does not exist or is not serviced.")
  return newFlight

def enterFlightDetails(newFlight):
  pass

def enterPricePlanAndCalculateProfit(newFlight):
  pass

def clearData(airports, newFlight):
  sure = input("Are you sure you want to clear all flight data entered?").lower() == "y"
  if sure:
    main()
  else:
    mainMenu(airports, newFlight)
  
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


if __name__ == "__main__":
  """Entry point of program"""
  main()
# classTests()
