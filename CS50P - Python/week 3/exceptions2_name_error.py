"""
original problematic code

try:
    x = int(input("Enter value: "))

except ValueError:
    print("x is not an integer")
    print(f"x is {x}")

"""

try:
    x = int(input("Enter value: "))

except ValueError:
    print("x is not an integer")

else:
    print(f"x is {x}")

# fixed code