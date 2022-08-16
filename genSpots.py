import os 
import random

path = 'F:/GAB IV/Paymongo/ooparking-lot'
fileName = "randomSpots.txt"
f = open(fileName,"w+")

sizes = ["S", "M", "L"]
spots = []

for i in range(100):
	f.write("(" + str(random.randint(1,10)) + "," + str(random.randint(1,10)) + "," + str(random.randint(1,10)) + "),")
	spots.append(i)
f.write("\n\n\n")

for i in range(100):
	f.write('"' + str(sizes[random.randint(0,2)]) + '", ')

f.write("\n\n\n")

occupied = random.sample(spots,k=90)	# Modify k to number of occupied spots
print("Occupied slots: " + str(len(occupied)))
print("Spots: " + str(len(spots)))
available = [i for i in spots if i not in occupied]
print("Available slots: " + str(len(available)))
f.write(str(occupied))
f.close()

print("Random Spots generated!")
