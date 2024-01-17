//text-cleaner.c

#include <stdio.h>
#include <ctype.h>


//prototypes
void text_cleaner(FILE *input, FILE *output);

int main() {

	text_cleaner(stdin, stdout); //calls text_cleaner function
	return 0;
}


//function reads character by character from the standard input and sends a cleaner verison to the standard output.
//a cleaner version means there is no punctuation or uppercase letters.
void text_cleaner(FILE *input, FILE *output) {
	
	int character;
	while((character = fgetc(input)) != EOF) { //iterates through each character in the input file until the end of input

		if(ispunct(character)) {

			//skipped the punctuation character to remove it in the output.
		
		} else if(isupper(character)) { //checks to see if the character is an upper case

			//if the character is an upper case, then it is changed to a lowercase and printed to the output
			character = tolower(character);
			fputc(character, output);

		} else { //in this case, it is a regular character

			//prints the character to output
			fputc(character, output);
		}
	}
}

