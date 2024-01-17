#! /usr/bin/env python3

import os
import sys

def index_files(index_directory):

	"""
	Loads and reads the sorted_documents.txt, sorted_terms.txt and td_matrix.txt
	
		Parameters: 
			index_directory: index directory
		
		Return Value:
			sorted_documents: list that stores the sorted documents from sorted_documents.txt
			sorted_terms: list that stores the sorted terms from sorted_terms.txt
			td_matrix: stores the term-document matrix from td_matrix.txt
	"""

	sorted_documents = []
	sorted_terms = []
	td_matrix = []

	with open(os.path.join(index_directory, 'sorted_documents.txt'), 'r') as sorted_documents_file: #reads the sorted documents from sorted_documents.txt
		sorted_documents = [line.strip() for line in sorted_documents_file]

	with open(os.path.join(index_directory, 'sorted_terms.txt'), 'r') as sorted_terms_file: #reads the sorted terms from sorted_terms.txt
		sorted_terms = [line.strip() for line in sorted_terms_file]

	with open(os.path.join(index_directory, 'td_matrix.txt'), 'r') as td_matrix_file: #reads the term-document matrix from td_matrix.txt
		for line in td_matrix_file:
			row = [int(value) for value in line.strip().split()]
			td_matrix.append(row)

	return sorted_documents, sorted_terms, td_matrix


def query_vector_function(sorted_terms):

	"""
	Reads the input from stdin with the term frequencies of the preprocessed query, and converts it into a query vector
	
		Parameters: 
			sorted_terms: list containing the sorted terms
		
		Return Value:
			query_vector: query vector
	"""

	frequency_dictionary = {} #dictionary to store term-frequency pairs

	for line in sys.stdin: #iterates over each line from standard input
		term, frequency = line.strip().split()
		frequency_dictionary[term] = int(frequency) #adds an entry to the frequency dictionary where term is the key and frequency is the value

	query_vector = []

	for term in sorted_terms: #iterates through each term is sorted_terms list to create the query vector
		frequency = frequency_dictionary.get(term, 0) #finds the frequency of the term and if the term is not found then the frequency is set to zero
		query_vector.append(frequency) #appends the frequency to the query vector

	return query_vector


def modify_matrix_vector(td_matrix):

	"""
	Removes the first column from the term-document matrix
	
		Parameters: 
			td_matrix: stores the term-document matrix
		
		Return Value:
			matrix_vector
	"""

	matrix_vector = td_matrix[1:] #makes a new vector without the first column

	return matrix_vector
	

def get_term_dictionary(term_lists, filenames):

	"""
	Creates a dictionary of the term frequencies for each file
	
		Parameters: 
			term_lists:
			filenames:
		
		Return Value:
			result_dictionary: 
	"""

	result_dictionary = {} #dictionary to store the term frequencies of each file
	
	for i, filename in enumerate(filenames): #iterates over each element in the filenames list (a list containing the names of the sorted documents)
		result_dictionary[filename] = [term_list[i] for term_list in term_lists] #iterates over the term_lists where each term_list is a list of term frequencies for each sorted document

	return result_dictionary


def cosine_similarity_calculation(vector_A, vector_B):
	
	"""
	Computes the cosine similarity calculation
	
		Parameters: 
			vector_A: used to compute calculation
			vector_B: used to compute calculation
		
		Return Value:
			result: answer of cosine similarity calculation 
	"""

	AB_sum = 0 #sum of the dot product of vectors A and B
	A_sum = 0 #sum of the modules of vector A
	B_sum = 0 #sum of the modules of vector B

	for index in range(len(vector_A)): #iterates over each element in the vectors
		AB_sum += vector_A[index] * vector_B[index] #calculates the sum of the dot product of vector A and vector B
		A_sum += vector_A[index] * vector_A[index] #calculates the sum of the modules of vector A
		B_sum += vector_B[index] * vector_B[index] #calculates the sum of the modules of vector B
	if AB_sum == 0: #if the sum of the dot product of vectors A and B are equal to 0, then return 0
		return 0;

	result = AB_sum / (A_sum**0.5 * B_sum**0.5) #calculate final result the cosine similarity

	return round(result, 4) #round the result to 4 decimal places and return it


def generate_ranking(query_vector, td_matrix_vector):

	"""
	Generates rankings based on cosine similarity values
	
		Parameters: 
			query_vector: query vector
			td_matrix vector: term-document vector
		
		Return Value:
			similarity_values_list: list that stores the calculated similarity values
	"""


	similarity_values_list = [] #list to store similarity values

	for text_file in td_matrix_vector: #iterates over each sorted document in the term-document matrix vector
		for q_val, td_val in zip(query_vector, td_matrix_vector[text_file]): #iterates over the pair q_val and td_val from the query vector, and sorted document names
			similarity_value = cosine_similarity_calculation(query_vector, td_matrix_vector[text_file]) #calculates the similarity value by calling the cosine_similarity_calculation function
		similarity_values_list.append(similarity_value) #store the similarity value in the similarity_values_list

	return similarity_values_list


def main():
	
	"""
	Checks number of command line arguments, calls the helper functions needed to complete this problem, prints the similarity values and text files (sorted documents)
	
		Parameters: 
			No parameters
		
		Return Value:
			None
	"""
	if len(sys.argv) != 2:
		print("Error")
		sys.exit(1)


	index_directory = sys.argv[1]
	
	sorted_documents, sorted_terms, td_matrix = index_files(index_directory)

	query_vector = query_vector_function(sorted_terms)

	td_matrix_vector = modify_matrix_vector(td_matrix)

	file_dictionary = get_term_dictionary(td_matrix_vector, sorted_documents)

	rankings = generate_ranking(query_vector, file_dictionary)


	result = list(zip(rankings, sorted_documents)) #combines the rankings and sorted documents
	result.sort(reverse=True)

	for similarity_value, text_file in result: #iterates over each similarity value and text file (sorted document) to print
		print(f"{similarity_value:.4f} {text_file}")


if __name__ == "__main__":
	main()

