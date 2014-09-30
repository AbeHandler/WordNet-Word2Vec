import sys


for line in sys.stdin:
    word = line.split(" ")[0]
    number = line.split(" ")[1]
    print word
    print number
