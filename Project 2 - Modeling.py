#Activity X.X.X:
#File:	<filename>.py
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

import math
import project2_methods

#inputs
volume = float(input("What is the part volume in cm^3? ")) #cm^3
volume = volume * 1000 #mm^3
tolerance = float(input("What are the part tolerances in mm? ")) #mm

#read data from text files and convert them to a list of lines
#FIX THESE
speed_data = open("Speed Data.txt", 'r')  #input("Print Speed data file: ")
aperature_data = open("Aperature Data.txt", 'r')
temp_data = open("Temperature Data.txt", 'r')

#converts text from input files to list of their lines
speed_lines = speed_data.readlines()
aperature_lines = aperature_data.readlines()
temp_lines = temp_data.readlines()

speed_data.close()
aperature_data.close()
temp_data.close()

#creates lists for speed, aperature, and temperature data
speed_x, speed_y = project2_methods.dataList(speedLines)
aperature_x, aperature_y = project2_methods.dataList(aperatureLines)
temp_x, temp_y = project2_methods.dataList(tempLines)

#determine coefficients of speed/aperature/temp for each equation type
speed_a0_lin, speed_a1_lin = project2_methods.Linear(speed_x, speed_y)
speed_a0_ex, speed_a1_ex = project2_methods.Exponential(speed_x, speed_y)
speed_a0_pow, speed_a1_pow = project2_methods.Power(speed_x, speed_y)

aperature_a0_lin, aperature_a1_lin = project2_methods.Linear( \
									 aperature_x, aperature_y)
aperature_a0_ex, aperature_a1_ex = project2_methods.Exponential( \
								   aperature_x, aperature_y)
aperature_a0_pow, aperature_a1_pow = project2_methods.Power(\
									 aperature_x, aperature_y)

temp_a0_lin, temp_a1_lin = project2_methods.Linear(temp_x, temp_y)
temp_a0_ex, temp_a1_ex = project2_methods.Exponential(temp_x, temp_y)
temp_a0_pow, temp_a1_pow = project2_methods.Power(temp_x, temp_y)

#determine r2 for each data set with the correct model type
#1 - linear, 2 - exponential, 3 - power
speed_r2, speed_func_type = project2_methods.r2(speed_a0_lin, speed_a1_lin, \
					   speed_a0_ex, speed_a1_ex, speed_a0_pow, speed_a1_pow, \
					   speed_x, speed_y)
aperature_r2, aperature_func_type = project2_methods.r2(aperature_a0_lin, \
					  aperature_a1_lin, aperature_a0_ex, aperature_a1_ex, 
					  aperature_a0_pow, aperature_a1_pow, \
					  aperature_x, aperature_y)
temp_r2, temp_func_type = project2_methods.r2(temp_a0_lin, temp_a1_lin, \
					 temp_a0_ex, temp_a1_ex, temp_a0_pow, temp_a1_pow, \
					 temp_x, temp_y)		

#determine function for speed/aperature/temp
speed_func = project2_methods.func(speed_a0_lin, speed_a1_lin, \
			 speed_a0_ex, speed_a1_ex, speed_a0_pow, speed_a1_pow, \
			 speed_func_type)	
aperature_func = project2_methods.func(aperature_a0_lin, \
				 aperature_a1_lin, aperature_a0_ex, aperature_a1_ex, 
				 aperature_a0_pow, aperature_a1_pow, \
				 aperature_func_type)				  
temp_func = project2_methods.func(temp_a0_lin, temp_a1_lin, \
			temp_a0_ex, temp_a1_ex, temp_a0_pow, temp_a1_pow, \
			temp_func_type)

#determine a tolerance buffer % based on the lowest r^2 value			
r2 = [speed_r2, aperature_r2, temp_r2]
tolerance_buffer = min(r2)			
					 
#give initial "best" values for speed/aperature/temp/time/error
best_speed = 99999999999
best_aperature = 9999999999999
best_temp = 9999999999999
best_time = 99999999999
dimension_error = 0

#run through every combination of speed/aperature/temp to
#find the lowest time while staying within tolerance
speed = speed_x[0]
while speed <= speed_x[len(speed_x)-1]:
	aperature = aperature_x[0]
	while aperature <= aperature_x[len(aperature_x)-1]:
		temp = temp_x[0]
		while temp <= temp_x[len(temp_x)-1]:
			#calculate error with each variable
			speed_error = speed_func(speed)
			aperature_error = aperature_func(aperature)
			temp_error = temp_func(temp)
			
			#calculate total dimension error
			dim_error = speed_error + aperature_error + temp_error
			if(dim_error > (tolerance*tolerance_buffer)):
				break
			
			#calculate print/production time
			#convert speed from sec to min
			print_time = volume/(speed * 60 * aperature) #min
			cure_time = 1570/temp + 20 #min
			if(print_time < cure_time):
				production_time = cure_time #min
			else:
				production_time = print_time + 20 #min

			#reassign "best" combination if new time is fater than old time
			if(production_time < best_time):
				best_time = production_time #min
				dimension_error = dim_error #mm
				best_speed = speed #mm/s
				best_aperature = aperature #mm^2
				best_temp = temp #C
				
			temp += .25
		aperature += 0.005
	speed += 0.005
	
#cost calculations
volume_cost = 500/1000 #$/mm^3
time_cost = 18 #$/min part is in machine
total_cost = volume_cost * volume + time_cost * best_time #USD

#output
print("Head Speed: ", round(best_speed, 3), " mm/s")
print("Head Aperature: ", round(best_aperature, 3), " mm^2")
print("Culture Temperature: ", best_temp, "C")
print("Estimated Production Time: ", round(best_time, 3), "min")
print("Estimated Part Dimensional Error: ", round(dimension_error,3), "mm")
print("Estimated Part Cost: $", round(total_cost,2))