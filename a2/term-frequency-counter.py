#! /usr/bin/env python3

import sys


def frequency_counter():
	"""
	Reads line by line from the standard input and stores the count of each word in a dictionary. Whenever the function finds a word already in the dictionary, the current value associated with the 
	key (word) is increased by 1.

		Parameters: 
			No parameters
	
		Return Value: 
			count: Dictionary
	"""

	count = {} #initialized an empty dictionary to store the word counts

	for line in sys.stdin: #iterates through each line in from the standard input

		line = line.strip()
		words = line.split()

		for word in words: #iterates through each word in the list of words
            
			if word in count: #if the word is already a key in the directory, increment by one because the word is a duplicate
                		count[word] = count[word] + 1

			else: #if the word is not already a key in the dictionary, the word is added to the dictionary and the count is set to 1 since it is not a duplicate
				count[word] = 1


	return count



def print_output(count):
	"""
	The keys (words) are sorted lexicographically in the dictionary. Prints the output.
	
		Parameters: 
			count: Dictionary
		
		Return Value:
			None
	"""

	sort_words = sorted(count.keys()) #sort the keys of the dictionary lexicographically

	for word in sort_words: #iterates through each word in all the sorted words
		print(word, count[word])
	
	

def main():
	"""
	Calls functions frequency_counter and print_output.
		
		Parameters: 
			No parameters
	
		Return Value:
			None
	"""

	count = frequency_counter()
	print_output(count)


if __name__ == "__main__":
	main()



	

