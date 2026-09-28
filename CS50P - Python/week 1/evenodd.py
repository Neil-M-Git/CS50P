def main():
    x = int(input("Enter a number = "))
    if is_even(x):
        print("Even no.")

    else:
        print("Odd no.")


def is_even(n):
    return n%2 == 0
    
main()