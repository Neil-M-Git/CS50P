# creating a personal simple python module

def main():
    hello("Dean")
    goodbye("Dean")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"Goodbye, {name}")

if __name__ == "__main__":
    main()