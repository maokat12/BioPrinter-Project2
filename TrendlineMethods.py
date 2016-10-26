import math

def Linear(data_x, data_y):
  #y = a_0 + a_1*x
  
  x_sum, y_sum, xy_sum, x2_sum = 0, 0, 0, 0
  for i, j in zip(data_x, data_y):
    x_sum = x_sum + i
    x2_sum = x2_sum + i**2
    y_sum = y_sum + j
    xy_sum = xy_sum + i*j
    
  n = len(data_x)
  a0 = ((y_sum * x2_sum) - (x_sum * xy_sum))/((n * x2_sum) - (x_sum * x_sum))
  a1 = ((n * xy_sum) - (y_sum * x_sum))/((n * x2_sum) - (x_sum * x_sum))
  return a0, a1
  
def Exponential(data_x, data_y):
  #y = a0*e^(a1*x)
  
  x_sum, lny_sum, xlny_sum, x2_sum = 0, 0, 0, 0
  for i, j in zip(data_x, data_y):
    x_sum = x_sum + i
    x2_sum = x2_sum + i**2
    lny_sum = lny_sum + math.log(j)
    xlny_sum = xlny_sum + i*math.log(j)
  
  n = len(data_x)
  a0 = math.exp(((lny_sum * x2_sum) - (x_sum * xlny_sum))/((n * x2_sum) - (x_sum * x_sum)))
  a1 = ((n * xlny_sum) - (lny_sum * x_sum))/((n * x2_sum) - (x_sum * x_sum))
  
  return a0, a1
  
def Power(data_x, data_y):
  #y = e^a0*x^a1
  
  lnx_sum, lny_sum, lnxlny_sum, lnx2_sum = 0, 0, 0, 0
  for i, j in zip(data_x, data_y):
    lnx_sum = lnx_sum + math.log(i)
    lnx2_sum = lnx2_sum + (math.log(i))**2
    lny_sum = lny_sum + math.log(j)
    lnxlny_sum = lnxlny_sum + math.log(i)*math.log(j)
    
  n = len(data_x)
  a0 = math.exp(((lny_sum * lnx2_sum) - (lnx_sum * lnxlny_sum))/((n * lnx2_sum) - (lnx_sum * lnx_sum)))
  a1 = ((n * lnxlny_sum) - (lny_sum * lnx_sum))/((n * lnx2_sum) - (lnx_sum * lnx_sum))
  
#method converts list of lines(x,y data) to a list consisting of two lists(x, y)
def dataList(lines):
  for j in lines:
	  k = j.split()
	  x.append(int(k[0]))
	  y.append(int(k[1]))
  datalist = [x, y]
  return datalist, x, y