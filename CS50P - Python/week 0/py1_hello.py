#def greet(to):
#    print("Hello", to)

#name = input("What's your name? ")
#greet(name)

def main():
    name = input("Enter your name: ")
    greet(name)

def greet(to = "world"):
    print("Hello", to)

main()