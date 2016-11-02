import math
import project2_methods

#uses excel sheet to analyze and display error points
#read data from text files and convert them to a list of lines
print("Program takes in CLEANED data files that have only datapoints.")
print("Please remove any titles or other text before inputting data files")
speed_data = open("Speed Data.txt", 'r')
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
speed_x, speed_y = project2_methods.dataList(speed_lines)
aperature_x, aperature_y = project2_methods.dataList(aperature_lines)
temp_x, temp_y = project2_methods.dataList(temp_lines)

#determine coefficients of speed/aperature/temp for each equation type
speed_a0_lin, speed_a1_lin = project2_methods.Linear(speed_x, speed_y)
speed_a0_ex, speed_a1_ex = project2_methods.Exponential(speed_x, speed_y)
speed_a0_pow, speed_a1_pow = project2_methods.Power(speed_x, speed_y)

speed_a0_lin = 0 #if the speed is 0, the dimension error should also be 0

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
			
#Cotter's Method
#set mins and maxs for speed/aperature/temp
speed_min = 0.005 #mm/s
speed_max = 3 #mm/s
aperature_min = 0.01 #mm^2
aperature_max = 2 #mm^2
temp_min = 4 #C
temp_max = 36 #C

#calculate dimension error using different combinations of mins/max
dim_1=(speed_func(speed_min)+aperature_func(aperature_min)+temp_func(temp_min))
dim_2=(speed_func(speed_min)+aperature_func(aperature_min)+temp_func(temp_max))
dim_3=(speed_func(speed_min)+aperature_func(aperature_max)+temp_func(temp_min))
dim_4=(speed_func(speed_min)+aperature_func(aperature_max)+temp_func(temp_max))
dim_5=(speed_func(speed_max)+aperature_func(aperature_min)+temp_func(temp_min))
dim_6=(speed_func(speed_max)+aperature_func(aperature_min)+temp_func(temp_max))
dim_7=(speed_func(speed_max)+aperature_func(aperature_max)+temp_func(temp_min))
dim_8=(speed_func(speed_max)+aperature_func(aperature_max)+temp_func(temp_max))

#prints different dimension error extremes
print(dim_1)
print(dim_2)
print(dim_3)
print(dim_4)
print(dim_5)
print(dim_6)
print(dim_7)
print(dim_8)