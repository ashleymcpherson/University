#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

    /*
     * variable to store the final answer
     */
    long int factorial = 1;

    /*
     * WRITE YOUR CODE TO DO COMMAND LINE INPUT CHECKING HERE
     */
    if (argc < 2) {
        printf("usage: %s <length> <length>\n", argv[1]);
        exit(1);
    }
    

    /*
     * Takes the command line input and converts it into int.
     */
    int num = atoi(argv[1]);


    /*
     * WRITE YOUR CODE TO DO THE FACTORIAL CALCULATIONS HERE
     */

    if(num < 0) {
	printf("error, factorials of negative numbers do not exist");
    } else {

    	for(int i = 1; i <= num; i++) {
	    factorial *= i;
    	}

    	printf("%ld\n", factorial);
    }
}
