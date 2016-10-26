import math
import TrendlineMethods

#inputs
volume = float(input("What is the part volume?")) #cm^3
volume = volume * 1000 #mm^3
tolerance = float(input("What are the part tolerances?")) #mm

#fixed costs
volume_cost = 500/1000 #$/mm^3
time_cost = 18 #$/min part is in machine

#initiate variables
aperature = 0 #mm^2
speed = 0 #mm/sec
temp = 0 #C

#read data from text files and convert them to a list of lines
speedData = open(input("Print Speed data file: "), 'r')
speedLines = speedData.readlines()
aperatureData = open(input("Print Aperature data file: "), 'r')
aperatureLines = aperatureData.readlines()
tempData = open(input("Culture Temperature data file: "), 'r')
tempLines = tempData.readlines()
speedData.close()
aperatureData.close()
tempData.close()

#declares lists for speed, aperature, and temperature data
speedList, speed_x, speed_y = dataList(speedLines)
aperatureList, aperature_x, aperature_y = dataList(aperatureLines)
temperatureList, temperature_x, temperature_y = dataList(tempLines)

speed_a0, speed_a1 = Linear(speed_x, speed_y)
aperature_a0, aperature_a1 = Exponential(aperature_x, aperature_y)
temp_a0, temp_a1 = Power(temperature_x, temperature_y)

best_speed, best_aperature, best_temp = 999, 999, 999
best_time, dimension_error = 999, 0
for speed in range(0, speed_x[len(speed_x)-1], 0.005):   #should the range numbers be hardcoded in?
	for aperature in range(0, aperature_x[len(aperature_x)-1], 0.005):
		for temperature in range(4, 36, .25):  #range numbers can be harded in here	
			speed_error = speed_a0 + speed_a1*speed
			aperature_error = math.exp(aperature_a0) * math.exp(aperature_a1*aperature)
			temp_error = math.exp(temp_a0) * temperature**temp_a1
			
			dim_error = speed_error + aperature_error + temp_error
			if(dim_error > tolerance):
				break
			
			print_time = volume/(speed * aperature) #min
			cure_time = 1570/temperature + 20 #min
			if(print_time < cure_time):
				production_time = cure_time #min
			else:
				production_time = print_time + 20 #min
			
			if(production_time < best_time)
				best_time = production_time
				dim_error = dimension_error
				best_speed = speed
				best_aperature = aperature
				best_temp = temp
				
#cost calculations
total_cost = volume_cost * volume + time_cost * best_time #USD
			
#output
print("Head Speed: " + head_speed)
print("Head Aperature: " + aperature)
print("Culture Temperature: " + temp)
print("Estimated Production Time: " + best_time)
print("Estimated Part Dimensional Error: " dimension_error)
print("Estimated Part Cost: $" + total_cost)