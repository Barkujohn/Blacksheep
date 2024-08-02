#BMI Calculator

height = float(input('Enter height in meters: '))
weight = float(input('Enter weight in kilograms: '))
BMI = weight/(height)**2
print(BMI)
if BMI >= 30:
    print('Obesity')
elif BMI >= 25 and BMI <= 29:
    print('Overweight')
elif BMI >= 18.5 and BMI <= 25:
    print('Normal')
else:
    print('Underweight')


# City Checker

Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai","Bangalore", "Chennai","Delhi"]

# Part 2

City_name = input('Enter a city name: ').title()

if City_name in Australia:
    print(f'{City_name} is in Australia')

elif City_name in UAE:
    print(f'{City_name} is in UAE')
 
elif City_name in India:
    print(f'{City_name} is in India')    
    
else:
    print('Invalid City')
    
    
# Part 3

first_city = input('Enter the first city name: ').title()
second_city = input('Enter the second city name: ').title()

if first_city in Australia and second_city in Australia:
    print('Both cities are in Australia')

elif first_city in UAE and second_city in UAE:
    print('Both cities are in UAE')
 
elif first_city in India and second_city in India:
    print('Both cities are in India')    
    
else:
    print("They don't belong to the same country")
    