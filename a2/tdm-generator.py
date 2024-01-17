#! /usr/bin/env python3

import os
import sys


def text_into_terms(text):

	"""
	Splits the text into terms.
	
		Parameters: 
			text: string with text
		
		Return Value:
			terms: a list of individual terms from the text string
	"""

	terms = text.split()
	return terms


def tdm_generator(input_directory, output_directory):

	"""
	Makes the matrix from input text files within an input directory. 
	
		Parameters: 
			input_directory: the input directory
			output_directory: the output directory 
		
		Return Value:
			None
	"""
	
	files = os.listdir(input_directory) #files is a list with all the names of the input files
	text_files = [filename for filename in files if filename.endswith('.txt')] #text_files is a list that contains only the names of files that are text files
	filenames = sorted(text_files)

	terms = set() #terms stores the unique words
	term_list = [] #term_list is a list that stores the unique words
	term_frequencies = {} #term_frequencies is a dictionary to count the frequency of each unique word
	number_of_columns = len(filenames)	
	number_of_rows = len(term_list)

	for file_index, filename in enumerate(filenames): #Iterates through each text file
		with open(os.path.join(input_directory, filename), 'r') as file: #reads text file the loop is currently on
			lines = file.readlines()	
			for line in lines: #iterates through each line 
				line = line.strip()
				term, frequency = line.split(' ')
				if term.isalnum() and not term.isnumeric(): #if the term we are analyzing is only letters and digits
					terms.add(term)
					#determines if the term is a key in the dictionary term_frequencies. If it does, it will find its value. If it doesn't, it returns a list of 0s
					term_frequencies[term] = term_frequencies.get(term, [0] * number_of_columns)
					term_frequencies[term][file_index] = frequency  #updates the dictionary with the frequency 

	term_list = sorted(terms)
	term_list.sort()

	number_of_columns = len(filenames)	
	number_of_rows = len(term_list)

	matrix = [] #initializes a matrix
	for index_row in range(number_of_rows):
		row = [0] * number_of_columns
		matrix.append(row)

	for term_index, term in enumerate(term_list): #iterates through each term
		matrix[term_index] = term_frequencies[term] #the list of frequencies with each word is assigned to the particular term index in the matrix
	
	with open(os.path.join(output_directory, "td_matrix.txt"), 'w') as output_file: #saves the term-document matrix in td_matrix.txt
		output_file.write("{} {}\n".format(number_of_rows, number_of_columns))
		for row in matrix:
			output_file.write(" ".join(map(str, row)) + "\n")

	with open(os.path.join(output_directory, "sorted_terms.txt"), 'w') as output_file: #saves all unique terms into sorted_terms.txt
		for term in term_list:
			output_file.write(term + "\n")
			
	with open(os.path.join(output_directory, "sorted_documents.txt"), 'w') as output_file: #saves all filenames from the input directory path into sorted_documents.txt
		for filename in filenames:
			output_file.write(filename + "\n")

def main():

	"""
	Checks number of command line arguments, checks if output directory exists, and calls tdm_generator.
	
		Parameters: 
			No parameters
		
		Return Value:
			None
	"""

	if len(sys.argv) != 3:
		print("Error")
		sys.exit(1)

	input_directory = sys.argv[1]
	output_directory = sys.argv[2]

	if not os.path.exists(output_directory):
		os.makedirs(output_directory)

	tdm_generator(input_directory, output_directory)

if __name__ == "__main__":
	main()

