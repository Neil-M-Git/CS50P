# implementing cmd line args with multiple inputs using sys module

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:                    # 1 cause the 0th idx will be the file name
    print("Hello, my name is", arg)