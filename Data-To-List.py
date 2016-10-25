#method converts list of lines(x,y data) to a list consisting of two lists(x, y)
def dataList(lines):
  for j in lines:
	  k = j.split()
	  x.append(int(k[0]))
	  y.append(int(k[1]))
  datalist = [x, y]
  return datalist, x, y

#read data from text files and convert them to a list of lines
a = open(input("Print Speed data file: "), 'r')
speedLines = a.readlines()
b = open(input("Print Aperature data file: "), 'r')
aperatureLines = b.readlines()
c = open(input("Culture Temperature data file: "), 'r')
tempLines = c.readlines()
a.close()
b.close()
c.close()

#declares lists for speed, aperature, and temperature data
speed, speed_x, speed_y = dataList(speedLines)
aperature, aperature_x, aperature_y = dataList(aperatureLines)
temperature, temperature_x, temperature_y = dataList(tempLines)