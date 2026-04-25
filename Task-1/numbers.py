# Q1: Use format function to format number 145 with 'o'
result = format(145, 'o')
print("Formatted result:", result)
print("Representation used: Octal")


# Q2: Calculate area of circular pond and total water
radius = 84
pi = 3.14

area = pi * radius * radius
water_per_sq_meter = 1.4

total_water = int(area * water_per_sq_meter)

print("\nArea of pond:", area)
print("Total water (liters):", total_water)


# Q3: Calculate speed in meters per second
distance = 490   # meters
time_minutes = 7
time_seconds = time_minutes * 60

speed = int(distance / time_seconds)

print("\nSpeed (m/s):", speed)
