import math
import TrendlineMethods

def dataList(lines):
  x, y = [], []
  for j in lines:
	  k = j.split()
	  x.append(float(k[0]))
	  y.append(float(k[1]))
  datalist = [x, y]
  return datalist, x, y

a = read("numbers.txt")
aLines = a.readlines()
a.close

aList, aX, aY = dataList(aLines)

print(aList)
print(aX)
print(aY)