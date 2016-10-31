#Activity: Project
#File:	project2_methods.py
#Date:
#By:	Katie Mao
#		mao86
#		Alex Greer
#		greer21
#		Nathan Hess
#		Hess35
#		Elizabeth Pulsifer
#		epulisfe
#
#ELECTRONIC SIGNATURE
#Katie Mao
#Alex Greer
#Nathan Hess
#Elizabeth Pulsifer

#The electronic signature oabove indicates that the program
#submitted for evaluation is my individual work.  I have
#a general understanding of all aspects of its development
#and execution.
#
#A BRIEF DESCRIPTION OF WHAT THE PROGRAM OR FUNCTION DOES
#A library of all methods used in the project2_model program.

import math

#find a0, a1 for a linear function given and x and y data set
def Linear(data_x, data_y):
  #y = a_0 + a_1*x
  
  #find the sum of x, y, xy, x^2
  x_sum, y_sum, xy_sum, x2_sum = 0, 0, 0, 0
  for i, j in zip(data_x, data_y):
    x_sum = x_sum + i
    x2_sum = x2_sum + i**2
    y_sum = y_sum + j
    xy_sum = xy_sum + i * j
	
  #length of data list x
  n = len(data_x) 
  
  #calculate a0, a1
  a0 = ((y_sum * x2_sum) - (x_sum * xy_sum))/((n * x2_sum) - (x_sum * x_sum))
  a1 = ((n * xy_sum) - (y_sum * x_sum))/((n * x2_sum) - (x_sum * x_sum))
  
  return a0, a1
  
#find a0, a1 for an exponential function given and x and y data set
def Exponential(data_x, data_y):
  #y = e^a0*e^(a1*x)
  
  #find the sum of x, ln(y), x * ln(y), x^2
  x_sum, lny_sum, xlny_sum, x2_sum = 0, 0, 0, 0
  for i, j in zip(data_x, data_y):
    x_sum = x_sum + i
    x2_sum = x2_sum + i**2
    lny_sum = lny_sum + math.log(j)
    xlny_sum = xlny_sum + i * math.log(j)
  
  #length of data list x
  n = len(data_x) 
  
  #calculate a0, a1
  a0 = math.exp(((lny_sum * x2_sum) - (x_sum * xlny_sum)) \
				/((n * x2_sum) - (x_sum * x_sum)))
  a1 = ((n * xlny_sum) - (lny_sum * x_sum))/((n * x2_sum) - (x_sum * x_sum))
  
  return a0, a1

#find a0, a1 for a power function given and x and y data set  
def Power(data_x, data_y):
  #y = a0*x^a1
  
  #find the sum of ln(x), ln(y), ln(x) * ln(y), ln(x)^2
  lnx_sum, lny_sum, lnxlny_sum, lnx2_sum = 0, 0, 0, 0
  for i, j in zip(data_x, data_y):
    lnx_sum = lnx_sum + math.log(i)
    lnx2_sum = lnx2_sum + (math.log(i))**2
    lny_sum = lny_sum + math.log(j)
    lnxlny_sum = lnxlny_sum + math.log(i) * math.log(j)
	
  #length of data list x
  n = len(data_x)
  
  #calculate a0, a1
  a0 = math.exp(((lny_sum * lnx2_sum) - (lnx_sum * lnxlny_sum)) \
				/((n * lnx2_sum) - (lnx_sum * lnx_sum)))
  a1 = ((n * lnxlny_sum) - (lny_sum * lnx_sum)) \
		/((n * lnx2_sum) - (lnx_sum * lnx_sum))

  return a0, a1
  
#method converts list of lines(x,y data) to a list consisting of two lists(x,y)
def dataList(lines):
  x = []
  y = []
  for j in lines:
	  k = j.split() #k - intermediate list with two inputs, x and y
	  x.append(float(k[0]))
	  y.append(float(k[1]))
  return x, y
  
#determine formula for the model type
def func(a0_lin, a1_lin, a0_ex, a1_ex, a0_pow, a1_pow, func_type):
	#determine which r2 is highest(which model best fits the data given)
	if func_type == 1:
		function = lambda x: a0_lin + a1_lin*x
	elif func_type == 2:
		function = lambda x: a0_ex * math.exp(a1_ex * x)
	else:
		function = lambda x: a0_pow * x**a1_pow
		
	return function
	
#finds the model type that best matches the given data set and
#returns the r2 value for that data set
def r2(a0_lin, a1_lin, a0_ex, a1_ex, a0_pow, a1_pow, x_list, y_list):
	#y = a_0 + a_1*x - linear
	#y = a0*e^(a1*x) - exponential
	#y = a0*x^a1 = power
	
	#find SST = SUM((y_i - y_bar)^2)
	#find average(y_bar)
	sum_y = 0
	for y in y_list:
		sum_y = sum_y + y
	y_bar = sum_y / len(y_list) #average
	
	#calculate SST
	SST = 0
	for y in y_list:
		SST = SST + (y - y_bar)**2
		
	#find SSE(linear, exponential, power)
	#SSE = SUM((y_i - f(x1))^2)
	SSE_lin = 0
	SSE_ex = 0
	SSE_pow = 0
	for x in x_list:
		SSE_lin = SSE_lin + (y_list[x_list.index(x)] - \
							(a0_lin + a1_lin * x))**2
		SSE_ex = SSE_ex + (y_list[x_list.index(x)] - \
						  (a0_ex * math.exp(a1_ex * x)))**2
		SSE_pow = SSE_pow + (y_list[x_list.index(x)] - \
							((a0_pow)*(x**a1_pow)))**2
	#calculate r2 of different model types
	r2_lin = 1 - SSE_lin / SST
	r2_ex = 1 - SSE_ex / SST
	r2_pow = 1 - SSE_pow / SST
	
	if r2_lin > r2_ex and r2_lin > r2_pow:
		r2 = r2_lin
		func_type = 1
	elif r2_ex > r2_lin and r2_ex > r2_pow:
		r2 = r2_ex
		func_type = 2
	else:
		r2 = r2_pow
		func_type = 3
		
	return r2, func_type
