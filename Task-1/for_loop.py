# Q1: Simulate rolling a die 20 times and count stats
import random

rolls = []
for i in range(20):
    rolls.append(random.randint(1, 6))

count_6 = rolls.count(6)
count_1 = rolls.count(1)

two_6_row = 0
for i in range(len(rolls) - 1):
    if rolls[i] == 6 and rolls[i+1] == 6:
        two_6_row += 1

print("Rolls:", rolls)
print("Number of 6s:", count_6)
print("Number of 1s:", count_1)
print("Two 6s in a row:", two_6_row)


# Q2: Jumping jacks workout
total = 0

for i in range(10):
    total += 10
    print("\nYou completed", total, "jumping jacks")

    if total == 100:
        print("Congratulations! You completed the workout")
        break

    tired = input("Are you tired? (yes/no): ")

    if tired.lower() == "yes" or tired.lower() == "y":
        skip = input("Do you want to skip remaining? (yes/no): ")
        if skip.lower() == "yes" or skip.lower() == "y":
            print("You completed a total of", total, "jumping jacks")
            break
        else:
            print("Remaining:", 100 - total)
