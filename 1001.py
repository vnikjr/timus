import sys
import math
data = sys.stdin.read().split()[::-1]
for i in range (len(data)):
    print (math.sqrt(int(data[i])))
