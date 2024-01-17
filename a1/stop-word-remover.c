/* stop-word-remover.c
* Echo the contents of file specified as the first argument, line by line. */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LEN 1000
#define MAX_LINES 1000
#define MAX_WORD_LEN 20000
#define MAX_WORDS 1000
int num_lines = 0;

//prototypes
void stop_word_remover(char *line);
int finding_stop_words(char *word);



int main(int argc, char *argv[]) {

	char lines[MAX_LINES][MAX_LINE_LEN];	
	char list_words[MAX_LINES][MAX_LINE_LEN];
	
	num_lines = 0;
	while (num_lines < MAX_LINES && fgets(lines[num_lines], sizeof(lines[0]), stdin) != NULL) { //reading the file and copying into a new array.
		strncpy(list_words[num_lines], lines[num_lines], sizeof(list_words[0]));
		stop_word_remover(list_words[num_lines]); //calling the stop_word_remover with the new array
		num_lines++;	
	}


	return 0;
}

/*
* Prints all the non-stop words
*/
void stop_word_remover(char *line) {
	char *token = strtok(line, " "); //splitting the line (one string) into each word (multiple little strings)
	int space_checker = 1; //used to check for a space at the beginning of each line
	
	while(token != NULL) {
		if(finding_stop_words(token) == 0) {
			if(space_checker != 1) { //checking for a space at the beginning of each line
				printf(" ");
			}
			printf("%s", token); //printing each non-stop word
			space_checker = 0; 
		}
	
		token = strtok(NULL, " ");
	}
	
}

/*
* Finds the stop words and returns back to the function stop_word_remover()
*/
int finding_stop_words(char *word) {
	char *stop_words[] = {"the", "a", "an", "of", "for", "to", "and", "but", "yet"};

	for(int i = 0; i < 9; i++) { //to determine if each word is a stop word
		if(strcmp(word, stop_words[i]) == 0) { //checks to see if the current word is a stop word
			return 1;
		}
	}
	return 0;
}


