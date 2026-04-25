# Q: Perform operations on Justice League list

justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# 1. Number of members
print("Number of members:", len(justice_league))


# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("\nAfter adding members:", justice_league)


# 3. Move Wonder Woman to beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("\nAfter making Wonder Woman leader:", justice_league)


# 4. Move Green Lantern between Aquaman and Flash
justice_league.remove("Green Lantern")
aquaman_index = justice_league.index("Aquaman")
justice_league.insert(aquaman_index + 1, "Green Lantern")
print("\nAfter separating Aquaman and Flash:", justice_league)


# 5. Replace with new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("\nNew team:", justice_league)


# 6. Sort list
justice_league.sort()
print("\nSorted team:", justice_league)

print("\nNew leader (0th index):", justice_league[0])
