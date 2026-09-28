# entering an integer to not except any other dt using try

try:
    x = int(input("Enter value: "))
    print(f"x is {x}")

except ValueError:
    print("x is not an integer")