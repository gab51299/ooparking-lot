import math

def surpassed24(a,b):
    return math.floor(a/24) < math.floor(b/24)

def nearest24(x):   #returns nearest multiple of 24
  return 24 * round(x/24)


a = float(input("Enter hour a: "))
b = float(input("Enter hour b: "))

#a = str(x(a))
#b = str(x(b))
if(surpassed24(a,b)):
    print("Exceeded a 24 chunk...")
    excess = b - nearest24(a)
    days = nearest24(a)/24
    print(str(days) + " days and " + str(excess) + " hrs")
else:
    print("Did not exceed a 24 chunk")