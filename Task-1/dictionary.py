# Q1: Create list of friends and convert to (name, length) tuples
friends = ["Arjun", "Ravi", "Kiran", "Suresh", "Vikram"]

name_length = []
for name in friends:
    name_length.append((name, len(name)))

print("Name and length tuples:", name_length)


# Q2: Expense tracking using dictionaries
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Total expenses
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("\nYour total expense:", your_total)
print("Partner total expense:", partner_total)

# Who spent more
if your_total > partner_total:
    print("You spent more")
elif partner_total > your_total:
    print("Your partner spent more")
else:
    print("Both spent equal")

# Find category with highest difference
max_diff = 0
max_category = ""

for key in your_expenses:
    diff = abs(your_expenses[key] - partner_expenses[key])
    if diff > max_diff:
        max_diff = diff
        max_category = key

print("Highest difference in:", max_category)
print("Difference amount:", max_diff)
