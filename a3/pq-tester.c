#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "list.h"
#include "emalloc.h"

#define MAX_LINE_LEN 5000

void inccounter(Patient *p, void *arg) {
    /* DO NOT CHANGE THIS FUNCTION. */
    int *ip = (int *)arg;
    (*ip)++;
}


void print_word(Patient *p, void *arg) {
    /* DO NOT CHANGE THIS FUNCTION. */
    char *fmt = (char *)arg;
    printf(fmt, p->name, p->birth_year, p->priority);
}


void dump(Patient *list) {
    /* DO NOT CHANGE THIS FUNCTION. */
    int len = 0;

    apply(list, inccounter, &len);    
    printf("Number of patients: %d\n", len);

    apply(list, print_word, "%s,%d,%d\n");
}

/*
 * Purpose: Tokenizes a line, distinguishes between enqueue and dequeue commands, builds the patient struct if enqueue command
 * Parameters: char *line - a pointer to a string that represents a line of input
 * Return: NULL; Patient *newest - a pointer to a patient structure
*/
Patient *tokenize_line(char *line) {
    /* TODO: You have to implement this function to tokenize a line
        and either:
        1) return a valid Patient pointer if the line command is enqueue
        2) return NULL if the line command is dequeue
    */

    char *token = strtok(line, ","); //tokenize the input line by ","
    
    //declare variables to hold the patient's information
    char *name;
    int birth_year;
    int priority;

    if(strcmp(token, "dequeue") == 0) { //if the token is a dequeue command, return NULL
        return NULL;
    } else if(strcmp(token, "enqueue") == 0) { //if the token is an enqueue command, extracts name, birth_year, and priority
        name = strtok(NULL, ",");
        birth_year = atoi(strtok(NULL, ","));
        priority = atoi(strtok(NULL, ","));

        Patient *newest = new_patient(name, birth_year, priority); //a new patient is made with the extracted name, birth_year, and priority
        return newest;
    }

    return 0;

}

/*
 * Purpose: Reads input from stdin, tokenizes and interprets each line, enqueue or dequeue patients in the list.
 * Parameters: Patient *list - pointer to priority queue
 * Return: Patient *list - pointer to updated priority queue
*/
Patient *read_lines(Patient *list) {
    /* TODO: You have to implement this function to tokenize all lines
        from the stdin. You HAVE TO use the tokenize_line function
        as an auxiliary function to parse each line.
        If tokenize_line returns a valid Patient pointer, add the
        patient to the list with the correct priority.
        Otherwise, dequeue the first patient from the list.
        At the end of the function, return the list to the caller.       
    */

    char line[MAX_LINE_LEN]; //buffer created to store each line
    
    while(fgets(line, sizeof(line), stdin) != NULL) { //reads the input from stdin
        Patient *patient = tokenize_line(line); //calls tokenize_line() to tokenize and interpret each line

        if(patient == NULL) { //if patient is NULL, then it is a dequeue command. Therefore, call removefront() to remove the patient at the front of the list
            list = remove_front(list); 
        } else { //else, then it is an enqueue command. Therefore, call add_with_priority() to add the patient to the list based on their priority
            list = add_with_priority(list, patient);
        }
    }
  
    return list;

}

/*
 * Purpose: Deallocates the memory
 * Parameters: Patient *list - a pointer to the head of the priority queue
 * Return: None
*/
void deallocate_memory(Patient *list) {
    /* TODO: You have to implement this function to deallocate (free) 
        memory from the list before the program ends
    */
    
    Patient *curr = NULL; //declare a current node
    for( ; list != NULL; list = list->next) { //frees the memory for the patient's name and current node
        curr = list;
        free(curr->name);
        free(curr);
    }

}


int main(int argc, char *argv[]) {
    /* DO NOT CHANGE THE MAIN FUNCTION. YOU HAVE TO IMPLEMENT YOUR
        CODE TO FOLLOW THE SEQUENCE OF INSTRUCTIONS BELOW. */
    Patient *list = NULL;

    if (argc != 1) {
            printf("Usage: %s\n", argv[0]);
            printf("Should receive no parameters\n");
            printf("Read from the stdin instead\n");
            exit(1);
    }

    list = read_lines(list);

 
    dump(list);
    
    deallocate_memory(list);

    exit(0); 
}
