# create an object for wind direction data and wind speed data
wind_dir = data.get('wind_dir')
wind_speed = data.get('wind_speed')

#create a variable that accepts user input
#call the variable userinput
userinput = input('What is your desired heading?')

#convert the user input to a float
userinput = float(userinput)

#calculate the difference between the user input and the wind direction
#call the variable wind_diff
wind_diff = userinput - wind_dir

