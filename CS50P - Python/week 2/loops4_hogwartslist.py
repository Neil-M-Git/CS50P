# printing student names at hogwarts with list and for loop

"""
# 1 - simple print

stud = ["Harry", "Ron", "Hermione", "Draco"]

for s in stud:
    print(s)
"""

# 2 - using the index range

stud = ["Harry", "Ron", "Hermione", "Draco"]

for i in range(len(stud)):   # will print based on indexes
    print(i + 1, stud[i])  # printing names from the no. 1