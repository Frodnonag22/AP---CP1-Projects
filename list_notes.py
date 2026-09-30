# AP Lists Tuples and Sets

# Lists
siblings = ["Alex", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake", "Jake"]
# Use brackets to make a list. Each item is separated by a comma. Each itm must be a proper item type.
length = len(siblings)
print(f"This is not my sibling: {siblings[2]}")
print(*siblings)
print(f"The youngest is {siblings[-1]}")
siblings.append("Gayshree")
siblings.insert(3, "Vienna")
siblings.extend(["Joe", "Israel", "Zee",])
siblings.remove("Vienna")
siblings.pop(0)
print(*siblings)

# Tuples
subjects = ("CP1", "CP2", "Advanced CP", "CSP", "Utah Studies", "US 1", "US 2", "World Civ", "World Geography", "CCA Business")
print(subjects[0])
print(*subjects)
#Tuples cannot be changed

#Sets
visited = {"Texas", "Ohio", "Minnesota", "Virginia", "D.C.", "Utah", "California", "Nevada"}
print(visited)
print(*visited)
print(len(visited))
visited.add("Idaho")
print(*visited)
visited.update({"Montana", "Arizona", "Oklahoma", "New Mexico"})
print(*visited)
visited.remove("Arizona")
print(*visited)

siblings = set(siblings)
siblings = list(siblings)
print(*siblings)