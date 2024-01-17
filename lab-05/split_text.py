#!/usr/bin/env python3

import sys

def split_text(inp):
	words = inp.split(",")
	
	for w in words:
		print(w)

def main():

    # Write your code here.  Refer to the hints provided
    # in the lab PDF.
	if len(sys.argv) != 2:
		print("Error")
		sys.exit(1)

	inp = sys.argv[1]
	split_text(inp)

if __name__ == "__main__":
	main()
