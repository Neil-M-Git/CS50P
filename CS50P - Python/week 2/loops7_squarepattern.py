# printing a square pattern using loops

def main():
    print_sq(4)

def print_sq(size):
    for i in range(size):     # For each row
        for j in range(size):     # For each col / brick
            print("#", end="")     # printing brick / pattern
        print()

main()