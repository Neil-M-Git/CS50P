# implementing cmd line args with the help of sys.argv fn from sys module (with if statement)

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("Hello, my name is", sys.argv[1])