while True:
    try:
        x = int(input("Enter value: "))

    except ValueError:
        print("x is not an integer")

    else:
        print(f"x is {x}")