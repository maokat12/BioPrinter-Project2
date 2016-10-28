import math
import TrendlineMethods

#inputs
volume = float(input("What is the part volume? ")) #cm^3
volume = volume * 1000 #mm^3
tolerance = float(input("What are the part tolerances? ")) #mm

#read data from text files and convert them to a list of lines
speedData = open(input("Print Speed data file: "), 'r')
aperatureData = open(input("Print Aperature data file: "), 'r')
tempData = open(input("Culture Temperature data file: "), 'r')

#converts text from input files to list of their lines
aperatureLines = aperatureData.readlines()
speedLines = speedData.readlines()
tempLines = tempData.readlines()

speedData.close()
aperatureData.close()
tempData.close()

#creates lists for speed, aperature, and temperature data
speedList, speed_x, speed_y = dataList(speedLines)
aperatureList, aperature_x, aperature_y = dataList(aperatureLines)
temperatureList, temp_x, temp_y = dataList(tempLines)

#determine coefficients of speed/aperature/temp for each equation type	
speed_a0_lin, speed_a1_lin = Linear(speed_x, speed_y)
speed_a0_ex, speed_a1_ex = Exponential(speed_x, speed_y)
speed_a0_pow, speed_a1_pow = Power(speed_x, speed_y)

aperature_a0_lin, aperature_a1_lin = Linear(aperature_x, aperature_y)
aperature_a0_ex, aperature_a1_ex = Exponential(aperature_x, aperature_y)
aperature_a0_pow, aperature_a1_pow = Power(aperature_x, aperature_y)

temp_a0_lin, temp_a1_lin = Linear(temp_x, temp_y)
temp_a0_ex, temp_a1_ex = Exponential(temp_x, temp_y)
temp_a0_pow, temp_a1_pow = Power(temp_x, temp_y)

#determine model(linear/exponential/power) for each dataset
speed_func = func_type(speed_a0_lin, speed_a1_lin, speed_a0_ex, speed_a1_ex, \
					   speed_a0_pow, speed_a1_pow, speed_x, speed_y)
aperature_func = func_type(aperature_a0_lin, aperature_a1_lin, aperature_a0_ex, \
					  aperature_a1_ex, aperature_a0_pow, aperature_a1_pow, \
					  aperature_x, aperature_y)
temp_func = func_type(temp_a0_lin, temp_a1_lin, temp_a0_ex, temp_a1_ex, \
				 temp_a0_pow, temp_a1_pow, temp_x, temp_y)


#find the best speed/time/aperature combination for the lowest time
#while staying within tolerance
#do we want to give a bit of buffer room in the tolerance?

#give initial "best" values for speed/aperature/temp/time/error
best_speed, best_aperature, best_temp = 999, 999, 999
best_time, dimension_error = 999, 0

#run through every combination of speed/aperature/temp to
#find the lowest time while staying withint tolerance
for speed in range(0, speed_x[len(speed_x)-1], 0.005):
	for aperature in range(0, aperature_x[len(aperature_x)-1], 0.005):
		for temperature in range(4, 36, .25):
			#calculate error with each variable
			speed_error = speed_func(speed)
			aperature_error = aperature_func(aperature)
			temp_error = temp_func(temp)
			
			#calculate total dimension error
			dim_error = speed_error + aperature_error + temp_error
			if(dim_error > tolerance):
				break
			
			#calculate print/production time
			#convert speed from sec to min
			print_time = volume/(speed * 60 * aperature) #min
			cure_time = 1570/temperature + 20 #min
			if(print_time < cure_time):
				production_time = cure_time #min
			else:
				production_time = print_time + 20 #min
			
			#reassign "best" combination if new time is fater than old time
			if(production_time < best_time):
				best_time = production_time #min
				dim_error = dimension_error #mm
				best_speed = speed #mm/s
				best_aperature = aperature #mm^2
				best_temp = temp #°C
				
#cost calculations
volume_cost = 500/1000 #$/mm^3
time_cost = 18 #$/min part is in machine
total_cost = volume_cost * volume + time_cost * best_time #USD

#test outputs
print(speed_func)
print(aperature_func)
print(temp_func)
			
#output
print("Head Speed: " + head_speed + " mm/s")
print("Head Aperature: " + aperature + " mm^2")
print("Culture Temperature: " + temp + "°C")
print("Estimated Production Time: " + round(best_time, 3) + "min")
print("Estimated Part Dimensional Error: " + round(dimension_error,3) + "mm")
print("Estimated Part Cost: $" + round(total_cost,2))
