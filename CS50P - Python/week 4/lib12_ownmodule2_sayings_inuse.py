import sys

from lib11_ownmodule1_sayings import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])