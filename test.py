import math
from datetime import datetime

cars = {}

class Car:
  def __init__(self, plate, size, timeIn=None, timeOut=None, spot=None, spotSize=None, runningTotal=None):
    self.plate = plate                  # unique identifier, plate number
    self.size = size                    # size of car
    self.timeIn = timeIn                # last timed in
    self.timeOut = timeOut              # last timed out
    self.spot = spot                    # current spot occupied
    self.spotSize = spotSize            # size of current spot occupied
    self.runningTotal = runningTotal    # running total of fee (for computation of returning parker)

    print("Created car with plate (" + plate + ") of size " + size)
    print("Current Cars: ")
    print(cars)
    # self.timeIn = None
    # self.timeOut = None
    # self.spot = None

# Initial cars
p1 = Car("ZSA703", "S")
p2 = Car("ABC123", "M")

cars["ZSA703"] = p1
cars["ABC123"] = p2

# Available car sizes
sizes = ["S", "M", "L"]

# Parking spot: Distances
parkingDistOG = [(6,8,3),
               (2,2,1),
               (1,2,9)]

parkingDist = [(8,10,6),(8,8,9),(3,10,9),(1,2,8),(4,10,2),(9,9,2),(8,5,2),(2,4,2),(6,5,1),(2,6,10),(1,2,7),(10,4,3),(4,6,3),(9,9,2),(4,7,3),(8,8,8),(8,7,1),(5,4,5),(3,7,4),(9,2,7),(8,5,4),(5,3,3),(1,6,10),(8,4,5),(4,3,7),(2,4,1),(7,3,8),(2,4,9),(6,5,4),(9,9,5),(8,6,9),(5,5,2),(10,9,1),(1,1,10),(6,4,2),(10,1,5),(6,4,8),(6,6,1),(10,6,5),(3,6,7),(1,3,7),(3,10,9),(6,2,3),(5,9,5),(3,6,2),(3,7,6),(4,6,7),(6,1,7),(10,4,2),(4,9,8),(4,5,6),(2,2,9),(7,8,9),(9,6,2),(10,1,4),(7,5,9),(10,1,7),(5,7,7),(1,1,4),(10,2,3),(7,4,7),(1,3,6),(6,8,5),(2,1,8),(5,1,9),(6,7,6),(9,8,2),(9,8,3),(1,9,3),(4,6,1),(7,5,8),(7,7,4),(8,8,5),(4,9,4),(7,5,5),(9,9,2),(5,8,7),(3,7,5),(5,6,1),(1,2,10),(5,9,8),(9,5,1),(5,8,6),(4,10,2),(9,2,1),(7,6,4),(9,6,10),(10,4,9),(10,9,6),(9,3,6),(6,2,7),(8,2,4),(5,9,2),(2,9,3),(9,6,2),(4,6,5),(9,1,10),(10,1,3),(4,4,9),(5,8,3)]

numOfEntrances = 3

# Parking spot: Sizes
parkingSizesOG = ["S", "M", "L"];
parkingSizes = ["S", "L", "S", "M", "M", "M", "M", "L", "S", "L", "L", "L", "S", "S", "S", "L", "S", "S", "M", "L", "L", "M", "S", "M", "L", "L", "L", "L", "L", "L", "L", "M", "S", "S", "S", "M", "L", "L", "M", "M", "S", "S", "M", "L", "S", "S", "M", "S", "M", "L", "L", "S", "S", "S", "M", "S", "S", "L", "S", "M", "S", "M", "S", "M", "M", "S", "L", "S", "L", "S", "M", "L", "L", "M", "M", "S", "M", "S", "L", "S", "L", "M", "L", "L", "S", "S", "M", "M", "M", "L", "L", "S", "L", "M", "M", "M", "L", "L", "L", "M"]



# List of available spots
available = [index for index, distances in enumerate(parkingDist)]

# FOR TESTING, randomly occupied spots
tempOccupiedforTesting = [87, 28, 3, 55, 39, 96, 56, 52, 32, 84, 80, 24, 18, 44, 16, 70, 72, 97, 36, 57, 74, 35, 2, 59, 73, 67, 27, 65, 33, 25, 69, 38, 99, 75, 11, 46, 14, 95, 81, 76, 43, 63, 71, 90, 45, 19, 41, 54, 21, 20, 15, 79, 7, 93, 26, 62, 9, 48, 82, 1, 4, 42, 50, 91, 10, 89, 17, 40, 53, 86, 37, 8, 0, 83, 61, 85, 31, 12, 13, 51, 22, 66, 88, 77, 34, 47, 94, 64, 60, 6]
available = [i for i in available if i not in tempOccupiedforTesting]
availableSizes = [size for index, size in enumerate(parkingSizes) if index in available]
displayAvailable = zip(available,availableSizes)
print("Vacant Spots: ")
for i in displayAvailable:
  print(i)

tempTime = 1000

############################# Methods #############################



def park(Car, entrance, time):
  print()
  print(Car.plate + " entering from entrance " + str(entrance) + "...")

  # Check parking time in, if recently left within 1 hr
  if(Car.timeOut is None):
    print(" - New Parking, time: " + str(time))
    Car.runningTotal = 0    # reset running total, no longer continues previous parking
    Car.timeIn = time
  elif((time - Car.timeOut).total_seconds()/3600 <= 60):   # Time since last timeout is less than an hour, modify this later
  
    print(" - HAS PARKED in past 1hr, prev timeIn: " + str(Car.timeIn))
    Car.timeOut = None      # reset timeOut, continue from last timeIn

  availableSpot = locateSpot(Car.size, entrance)

  # Occupy Spot
  Car.spot = availableSpot  # set Car's spot
  available.remove(availableSpot) # remove spot from available spots
  Car.spotSize = parkingSizes[availableSpot]  # assign spotsize for later computation of fee



def getExceedingFee(excessTime, size):
  print("Exceeded 3 hrs by: " + str(excessTime))
  print("excessTime type: " + str(type(excessTime)))
  excessTime = round(excessTime)
  fee = 0
  match size:
    case "S":
      fee += 20*(excessTime)
    case "M":
      fee += 60*(excessTime)
    case "L":
      fee += 100*(excessTime)
    case _:
      print("Invalid Size.")
  
  return fee



def unpark(Car, time):
  print()
  Car.timeOut = time 
  print("UNPARKING: " + str(Car.timeOut) + " - " + str(Car.timeIn))

  duration = (time - Car.timeIn).total_seconds()/3600

  print(Car.plate + " leaving at " + str(time) + ". Parked in " + Car.spotSize)
  print("Parked for duration: " + str(duration) + "hrs")
  print("New available spot: " + str(Car.spot))
  available.insert(0,int(Car.spot))

  fee = 40
  if(duration > 3 and duration < 24):
    #compute for exceeding
    additional = getExceedingFee(duration-3,Car.spotSize)

    fee += additional
    print("Additional Rate: " + str(additional) + ". Charging for rate of: " + Car.spotSize)
    
  elif(duration >= 24):
    #compute for overnight fee
    duration -= 3 # initial 3 hours
    exceedFee = math.floor(duration/24)*5000
    remainderFee = getExceedingFee(duration % 24,Car.spotSize)

    fee += exceedFee + remainderFee
    print("Overnight. Total: " + str(exceedFee) + " + " + str(remainderFee) + " = " + str(fee));
  else:
    fee = 40
  
  # Clear previous spot and spotsize for the car
  Car.spot = None
  Car.spotSize = None
  if(Car.runningTotal > 0):
    fee -= 40; # prevent repeating of initial 3hrs
  print("Running Total: " + str(Car.runningTotal) + " + Fee: " + str(fee))
  Car.runningTotal += fee
  print("Pay Php" + str(Car.runningTotal) + " at the exit. Thank you!")
  return Car.runningTotal



def doesFit(size1,size2):
  if((size1 == 'L' and size2 != 'L') or (size1 == 'M' and size2 == 'S')):
    return False
  else:
    return True



# Locates nearest available parking spot given a car's size and the entrance used
def locateSpot(size, entrance):
  # Shortest distance to an available spot given an entrance

  #shortestDist = min([spot[entrance] for index, spot in enumerate(parkingDist) if index in available])
  #print("Distance to nearest spot/s: " + str(shortestDist) + "m")\

  getDistances = [spot[entrance] for index, spot in enumerate(parkingDist) if index in available]   # get list of distances of parking spots to the entrance that are available
  getDistances.sort()   # sort them, since we want to find the closest
  distances = set(getDistances)  # remove duplicate distances

  print("Available parking spots:")
  print(distances)

  for i in distances:   # iterate over distances from the entrance
    print("Checking spots " + str(i) + "m away from entrance " + str(entrance))
    nearestSpots = [spot for spot in available if parkingDist[spot][entrance] == i]   # get spots n distance away from the parking
    print("Nearest Spots: " + str(nearestSpots))

    possibleSpot = chooseSizeSpot(nearestSpots, size) # will look at the sizes of the spots within a certain distance
    if(possibleSpot is not None):     # checks if the method returned None which indicates the car doesnt fit in the spots
      return possibleSpot

  return -1 # No spot found

# Obtain sizes of available close spots
def chooseSizeSpot(nearestSpots, size):
  spotsWithSize = []
  for spot in nearestSpots:
    # If current car fits, else dont include/consider spot
    print("Checking size...")
    print(size + " > " + parkingSizes[spot])
    if(doesFit(size,parkingSizes[spot])):
      spotsWithSize.insert(0,(spot, parkingSizes[spot]))  #tuple, containing the spot #, and the size of that spot

  # Sort by size for efficiency; assign smallest possible spot
  spotsWithSize.sort(key=lambda x: sizes.index(x[1]))     # sorts according to the sizes list = S, M, L
                                                          # sorts the spot size (x[1]) according to the sizes list

  if(len(spotsWithSize) <= 0): #check if there are no spots of usable size within n distance
    return None
  else:
    # Get first available smallest and nearest spot.
    print("Available parking spot found at #" + str(spotsWithSize[0][0]) + "!")
    return spotsWithSize[0][0]

def validate(plate):
  return (plate in cars.keys()) # check if car exists

def canPark(Car):
  # check if hasn't timed out yet, or if car already has a spot
  return (Car.timeOut is not None or Car.spot is None or Car.spotSize is None)

def canUnPark(Car):
  # check if car has timed in, and has a spot
  return (Car.timeIn is not None and Car.spot is not None and Car.spotSize is not None)

def entranceExists(entrance):
  return(entrance < numOfEntrances and entrance >= 0)

#park(p1, 2, tempTime)
#park(p2, 2, tempTime)

tempTime += 1000

#unpark(p2, tempTime)

tempTime += 6300
#unpark(p1, tempTime)


########################### Input Section ###########################

while(True):
  print()
  action = input("Action:  ").strip().upper()
  print()

  match action:
    case "P":     # Park
      plateNum = input("Enter plate number: ").strip().upper()
      currtime = str(input('Enter date(hhmm mmdd): ')).strip()
      my_date = datetime.strptime(currtime, "%H%M %m%d")

      print("DATE: " + str(my_date))
      
      entrance = int(input("Pick an entrance: "))

      if(validate(plateNum) and canPark(cars[plateNum]) and entranceExists(entrance)):  #validation to check if car exists, and can park, and entrance exists
        park(cars[plateNum], entrance, my_date)
      else:
        print("Invalid!")
        print(validate(plateNum))
        print(canPark(cars[plateNum]))
        print(entranceExists(entrance))
        print("Error. The given car or entrance does not exist, or cannot park.")
    case "U":     # Unpark
      plateNum = input("Enter plate number: ").strip().upper()
      currtime = str(input('Enter date(hhmm mmdd): ')).strip()
      my_date = datetime.strptime(currtime, "%H%M %m%d")

      print("MY_DATE")
      print(type(my_date))
      if(validate(plateNum) and canUnPark(cars[plateNum]) and entranceExists(entrance)):  #validation for unpark
        unpark(cars[plateNum], my_date)
      else:
        print("Error. The given car or entrance does not exist, or cannot park.")
    case "C":     # Create car
      plateNum = input("Enter plate number: ").strip().upper()
      carSize = input("Enter car size: ").strip().upper()

      cars[plateNum] = Car(plateNum, carSize)
    case _:
      print("Invalid action.")
  print()
