#!/usr/bin/env python3

import sys
import math

def pythag(a, b):
	hypotenuse = math.sqrt(a ** 2 + b ** 2)
	return hypotenuse

def main():
 
    # parse the command-line arguments
    # print an error and quit if there aren't the right number

    # convert the command line arguments from strings to floats

	if len(sys.argv) != 3:
		print("Error")
		sys.exit(1)

	try:
		a = float(sys.argv[1])
		b = float(sys.argv[2])
	except Error:
		print("Error")
		sys.exit(1)
    

	print("Sides ", a, " and ", b, ", hypotenuse ", end="", sep="")
	print("%.4f" % pythag(a, b))

if __name__ == "__main__":
	main()
