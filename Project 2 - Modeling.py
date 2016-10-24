import math

#inputs
volume = float(input("What is the part volume?")) #cm^3
volume = volume * 1000 #mm^3
tolerance = float(input("What are the part tolerances?")) #mm

#fixed costs
volume_cost = 500 #$/cm^3
volume_cost = 500/1000 #$/mm^3
time_cost = 18 #$/min part is in machine

#initiate variables
aperature = 0 #mm^2
head_speed = 0 #mm/sec
temp = 0 #C

#SUBJECT TO CHANGE
#error eqations
speed_error = 0.3949 * head_speed + 0.0848 #mm         
temp_error = math.exp(math.log(temp) - 11.209) #mm
aperature_error = math.exp(aperature - 5.2251) #mm
dimension_error = speed_error + temp_error + aperature_error #mm  dimension_error <= tolerance

#time equations
print_time = volume/(head_speed * aperature) #min
cure_time = 1570/temp + 20 #min
if(print_time < cure_time):
	production_time = cure_time #min
else:
	production_time = print_time + 20 #min
	
#cost calculations
total_cost = volume_cost * volume + time_cost * production_time #USD



#output
print("Head Speed: " + head_speed)
print("Head Aperature: " + aperature)
print("Culture Temperature: " + temp)
print("Estimated Production Time: " + production_time)
print("Estimated Part Dimensional Error: " dimension_error)
print("Estimated Part Cost: $" + total_cost)