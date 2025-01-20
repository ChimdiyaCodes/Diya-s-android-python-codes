def celsius_to_fahrenheit(x):
    y= x * 9/5 + 32
    return y

#Ask the user for the Celsius temperature
temp_in_celsius = float(input("Enter the temperature in Celsius: "))

#Convert to Fahrenheit using the function
temp_in_fahrenheit = celsius_to_fahrenheit(temp_in_celsius)

#Print the result
print(f"{temp_in_celsius}°C is equal to {temp_in_fahrenheit}°F")