import decimal
import sys

__author__ = "Reuben Taylor"


# Classes
class Airport:

  def __init__(self, IATACode, fullName, distanceFromLPL, distanceFromBOH):
    self.IATACode = str(IATACode).upper()
    self.fullName = str(fullName)
    self.distanceFromLPL = decimal.Decimal(distanceFromLPL)
    self.distanceFromBOH = decimal.Decimal(distanceFromBOH)

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
      case _:
        self.runningCostPer100KM = decimal.Decimal(0)
        self.maxFlightRange = 0
        self.allStandardCapacity = 0
        self.minFirstClassSeats = 0

  def __str__(self):
    return f"## Plane ##\nPlane Type: {self.planeType}\nRunning Cost/100km: {self.runningCostPer100KM}\nMax Flight Range: {self.maxFlightRange}\nCapacity If All Seats Are Standard: {self.allStandardCapacity}\nMinimum Number of First-Class Seats (if any): {self.minFirstClassSeats}"


class Flight:

  def __init__(self):
    self.UKAirport = "NONE"
    self.overseasAirport = Airport("NONE", "NONE", 0, 0)
    self.distance = decimal.Decimal(0)
    self.plane = Plane("None")
    self.firstClassSeats = 0
    self.standardClassSeats = self.plane.allStandardCapacity - self.firstClassSeats
    self.standardClassSeatPrice = decimal.Decimal(0)
    self.firstClassSeatPrice = decimal.Decimal(0)
    self.perSeatFlightCost = decimal.Decimal(0)
    self.totalFlightCost = decimal.Decimal(0)
    self.flightIncome = decimal.Decimal(0)
    self.flightProfit = decimal.Decimal(0)

  def setDistance(self):
    self.distance = self.overseasAirport.distanceFromLPL if self.UKAirport == "LPL" else self.overseasAirport.distanceFromBOH

  def setStandardClassSeats(self, firstClassSeats):
    self.firstClassSeats = firstClassSeats
    self.standardClassSeats = self.plane.allStandardCapacity - self.firstClassSeats

  def calculateCostsAndProfit(self):
    self.perSeatFlightCost = decimal.Decimal((self.plane.runningCostPer100KM * self.distance) / 100)
    self.totalFlightCost = self.perSeatFlightCost * (self.firstClassSeats +
                                                     self.standardClassSeats)
    self.flightIncome = (self.firstClassSeats * self.firstClassSeatPrice) + (self.standardClassSeats * self.standardClassSeatPrice)
    self.flightProfit = self.flightIncome - self.totalFlightCost

  def __str__(self):
    return f"## Flight ##\nFrom: {self.UKAirport}\nTo: {self.overseasAirport.IATACode}\nDistance: {self.distance}\n# Plane #\nPlane Type: {self.plane.planeType}\nMaximum Flight Range: {self.plane.maxFlightRange}\nRunning Cost/Seat/100km: {self.plane.runningCostPer100KM}\nCapacity If All Seats Are Standard: {self.plane.allStandardCapacity}\nStandard Class Seats: {self.standardClassSeats}\nStandard Class Seat Price: {self.standardClassSeatPrice}\nFirst Class Seats: {self.firstClassSeats}\nFirst Class Seat Price: {self.firstClassSeatPrice}\n# Income #\nFlight Cost Per Seat: {self.perSeatFlightCost}\nTotal Cost of Flight: {self.totalFlightCost}\nFlight Income: {self.flightIncome}\nFlight Profit: {self.flightProfit}"


def main():
  airports = readAirportData("Airports.txt")
  newFlight = Flight()
  mainMenu(airports, newFlight)


def readAirportData(fileName):
  airports = {}
  with open(fileName) as file:
    for line in file:
      newAirportAsList = str(line).split(",")
      newAirport = Airport(*newAirportAsList)
      airports[newAirport.IATACode] = newAirport
  return (airports)


def mainMenu(airports, newFlight):
  print(newFlight)
  choiceOfAction = input(
      "########## Main Menu ##########\nEnter a number to select the desired action.\n1 - Enter Airport Details\n2 - Enter Flight Details\n3 - Enter Price Plan and Calculate Potential Profit\n4 - Clear All Entered Data\n5 - Quit Program\n"
  )
  match choiceOfAction:
    case "1":
      newFlight = enterAirportDetails(airports, newFlight)
    case "2":
      newFlight = enterFlightDetails(newFlight)
    case "3":
      newFlight = enterPricePlanAndCalculateProfit(newFlight)
    case "4":
      clearData(airports, newFlight)
    case "5":
      print("Thank you for using the program. Goodbye.\n")
      sys.exit()
    case "X":
      print("Hello world")
    case _:
      print(f"'{choiceOfAction}' is an invalid choice of action.\n\n")
  mainMenu(airports, newFlight)


def enterAirportDetails(airports, newFlight):
  domesticAirportMenuSelection = input(
      "Enter a letter to select the domestic airport.\nL - Liverpool John Lennon (LPL)\nB - Bournemouth International (BOH)\n"
  )
  match domesticAirportMenuSelection:
    case "L":
      newFlight.UKAirport = "LPL"
    case "B":
      newFlight.UKAirport = "BOH"
    case _:
      print(f"'{domesticAirportMenuSelection}' is not a valid choice.")
      return newFlight
  selectedOverseasAirport = input(
      "Please enter the IATA code of the overseas airport.").upper()
  if len(selectedOverseasAirport) > 3:
    print(f"'{selectedOverseasAirport}' is not a valid IATA code.")
  else:
    try:
      newFlight.overseasAirport = airports[selectedOverseasAirport]
      newFlight.setDistance()
    except Exception:
      print(
          f"The airport with the IATA code {selectedOverseasAirport} does not exist or is not serviced."
      )
  return newFlight


def enterFlightDetails(newFlight):
  selectedAircraft = input(
      "Please select a type of aircraft from the following:\n1 - Medium Narrow Body\n2 - Large Narrow Body\n3 - Medium Wide Body\n"
  )
  match selectedAircraft:
    case "1":
      newFlight.plane = Plane("Medium Narrow Body")
    case "2":
      newFlight.plane = Plane("Large Narrow Body")
    case "3":
      newFlight.plane = Plane("Medium Wide Body")
    case _:
      print(f"'{selectedAircraft}' is not a valid choice of aircraft type.")
      return newFlight
  return newFlight


def enterPricePlanAndCalculateProfit(newFlight):
  if newFlight.UKAirport == "NONE":
    print("No domestic airport has been selected.")
  elif newFlight.overseasAirport == "NONE":
    print("No overseas airport has been selected.")
  elif newFlight.plane.planeType == "None":
    print("A plane has not been selected.")
  elif newFlight.firstClassSeats and newFlight.firstClassSeats < newFlight.plane.minFirstClassSeats:
    print("The minimum number of First-Class seats has not been met.")
  elif newFlight.plane.maxFlightRange < newFlight.distance:
    print(
        "The selected plane does not have enough range to reach the destination."
    )
  else:
    firstClassSeats = int(
        input(
            "Enter the number of First-Class seats you wish to have on the flight."
        ))
    if firstClassSeats and firstClassSeats < newFlight.plane.minFirstClassSeats:
      print("Too few First-Class seats entered.")
      return newFlight
    newFlight.setStandardClassSeats(firstClassSeats)
    firstClassSeatPrice = decimal.Decimal(
        input("Enter the price of a First-Class seat."))
    newFlight.firstClassSeatPrice = firstClassSeatPrice
    standardClassSeatPrice = decimal.Decimal(
        input("Enter the price of a Standard-Class seat."))
    newFlight.standardClassSeatPrice = standardClassSeatPrice
    newFlight.calculateCostsAndProfit()
    print(newFlight)
  return newFlight


def clearData(airports, newFlight):
  sure = input(
      "Are you sure you want to clear all flight data entered? (y/n)").lower() == "y"
  if sure:
    main()
  else:
    mainMenu(airports, newFlight)


if __name__ == "__main__":
  """Entry point of program"""
  main()
