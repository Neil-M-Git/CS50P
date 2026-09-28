def main():
    num = get_num()
    meow(num)

# get_num for user input
def get_num():
    while True:
        n = int(input("Enter number: "))
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("Meow")

main()