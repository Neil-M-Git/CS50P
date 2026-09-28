def main():
    x = int(input("Enter number: "))
    print("x square = ", sq(x))
    print("x cube = ", cube(x))

def sq(n):
    return pow(n, 2)
    
def cube(n):
    return pow(n, 3)

main()