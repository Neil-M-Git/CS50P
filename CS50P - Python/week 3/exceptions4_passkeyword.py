# defining a function for easier functionality

def main():
    x = get_int("Enter value: ")
    print(f"x is {x}")

def get_int(val):
    while True:
        try:
            x = int(input(val))
            return x

        except ValueError:
            pass # used to catch the error but pass, prompting the user for input again

main()