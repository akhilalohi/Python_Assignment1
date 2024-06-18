# Ask the user for the temperature value
temperature = float(input("Enter the temperature value: "))

# Ask the user for the conversion type
conversion_type = input("Enter 'C' to convert from Celsius to Fahrenheit or 'F' to convert from Fahrenheit to Celsius: ").strip().upper()

# Perform the conversion based on user input
if conversion_type == 'C':
    converted_temperature = (temperature * 9/5) + 32
    print("The temperature in Fahrenheit is:", converted_temperature)
elif conversion_type == 'F':
    converted_temperature = (temperature - 32) * 5/9
    print("The temperature in Celsius is:", converted_temperature)
else:
    print("Invalid input. Please enter 'C' or 'F'.")
