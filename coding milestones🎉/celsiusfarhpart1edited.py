def celsius_to_fahrenheit(x):
    y=x * 9/5 + 32
    return y
    
temp_in_celsius =30
temp_in_fahrenheit = celsius_to_fahrenheit (temp_in_celsius)

print (f"{temp_in_celsius}°C is equal to {temp_in_fahrenheit}°F")
