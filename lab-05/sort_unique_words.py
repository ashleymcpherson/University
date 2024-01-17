#! /usr/bin/env python3

import sys

def sort_unique_words():
	lists = []

	for line in sys.stdin:
		strings = line.split(",")
		for word in strings:
			word = word.strip()
			lists.append(word)
	
	sort = sorted(set(lists))
	return sort

def main():
    
    #  Read the words from sys.stdin
    #  Keep only the unique words
    #  Print them in sorted order.

	sort = sort_unique_words()

	for word in sort:
		print(word)

if __name__ == "__main__":
	main()
