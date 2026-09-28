x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))

ch = input("Enter operation (+, -, *, /, //, %): ")

match ch:
    case "+":
        print("Sum of x and y = ", x + y)

    case "-":
        print("Difference of x and y = ", x - y)

    case "*":
        print("Product of x and y = ", x * y)

    case "/":
        print("Answer after dividing x and y = ", x / y)

    case "//":
        print("Quotient after dividing x and y = ", x // y)

    case "%":
        print("Remainder after dividing x and y = ", x % y)