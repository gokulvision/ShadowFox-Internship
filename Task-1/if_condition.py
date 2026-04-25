# Q1: Calculate BMI and determine category
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))

bmi = weight / (height ** 2)

if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")


# Q2: Find which country a city belongs to
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("\nEnter a city name: ")

if city in Australia:
    print(city, "is in Australia")
elif city in UAE:
    print(city, "is in UAE")
elif city in India:
    print(city, "is in India")
else:
    print("City not found")


# Q3: Check if two cities belong to same country
city1 = input("\nEnter first city: ")
city2 = input("Enter second city: ")

def get_country(city):
    if city in Australia:
        return "Australia"
    elif city in UAE:
        return "UAE"
    elif city in India:
        return "India"
    else:
        return None

country1 = get_country(city1)
country2 = get_country(city2)

if country1 == country2 and country1 is not None:
    print("Both cities are in", country1)
else:
    print("They don't belong to the same country")
