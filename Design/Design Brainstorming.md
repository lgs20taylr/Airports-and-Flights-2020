[[[8520-3-PPT-Jun21-E1.pdf]]]
# Features
Calculates the profitability of flight between UK Airport (Bournemouth International and Liverpool John Lennon)
	![[Pasted image 20240428205923.png]]
# Flight Details
## Airports
- Create parent class airport with child UK and overseas classes
- UK airport
- overseas airport
	- [[Airports.txt]] containing data for overseas airports
		- ![[Overseas Airport Data.png]]
## Aircraft
![[Aircraft Type Data.png]]
## Seats
- number of first-class seats
	- each one takes up the space of two standard class seats 
- price of a first-class seat
- price of a standard-class seat.


# Design
## Classes
### Airport Class
`__str__`
IATA Code - string, 3 Letters, all caps
Airport Name - string
Distance from LPL - int
Distance from BOH - int
### Plane Class
`__init__` uses match case between MNB, LNB, and MWB and sets values accordingly
`__str__` 
Cost/Seat/100km - int
Maximum Range - int
All-Standard Capacity - int
Minimum First-Class Seats - int

### Flight Class
UK Airport - string (LPL or BOH)
Overseas Airport - Airport
Plane - Plane
First-Class Seats - int
Standard Class Seats - int `Capacity if all seats are standard-class – Number of first-class seats x 2`
Price of Seat (Standard) - Decimal
Price of Seat (First Class) - Decimal
Flight Cost Per Seat - Decimal `running cost per seat per 100 km (for the selected type of aircraft) × distance between the UK airport and the overseas airport / 100`
Flight Total Cost - Decimal `flight cost per seat × (number of first-class seats + number of standard- class seats)`
Flight Income - Decimal `number of first-class seats × price of a first-class seat + number of standard-class seats × price of a standard-class seat`
Flight Profit - Decimal `flight income - flight cost`

## Functions
### Main
#### Body
reads [[Airports.txt]] and converts each to an Airport Class Object and stores it in a hashmap with the IATA codes as keys
create flight object
move to Main Menu
### Main Menu
#### Parameters
hashmap of airports
flight object
#### Body
pick from using match case, sets flight object values using respective functions:
- Enter airport details
- Enter flight details
- Enter flight plan and calculate profit
- Clear data
- Quit

### Airport Details
#### Parameters
hashmap of airports
#### Body
user enters IATA code of UK airport
try:... except: 
user enters IATA code of Overseas
prints full name of airport
try:.. except: for validation
returns UK IATA code and airport object from hashmap
send them back to mm
### Flight Details
#### Body
user picks type of aircraft
plane object created with the data of the type of aircraft
data of plane object printed
user enters number of first class seats
if not 0:
	error if less than min first class in plane object
	error if more than half of capacity
	calculate number of standard class seats `Capacity if all seats are standard-class – Number of first-class seats x 2`
main menu
### Price Plan and Profit Calculation
validate the following:
	UK Airport exists
	Overseas Airport exists
	Plane exists
	max flight range of plane >= distance between UK and Overseas
enter price of first and standard class seats
calculate the following and stick ''em inside the flight object:
	Flight Cost Per Seat - Decimal `running cost per seat per 100 km (for the selected type of aircraft) × distance between the UK airport and the overseas airport / 100`
	Flight Total Cost - Decimal `flight cost per seat × (number of first-class seats + number of standard- class seats)`
	Flight Income - Decimal `number of first-class seats × price of a first-class seat + number of standard-class seats × price of a standard-class seat`
	Flight Profit - Decimal `flight income - flight cost`
print the flight object using it's `__str__` method
put them back to the main menu

### Clear Data
#### Body
access as globals and then deletes airport, plane, and flight plan
### Quit
#### Body
Says goodbye and quit the program (sys.exit)
