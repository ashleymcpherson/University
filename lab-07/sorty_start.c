#define _GNU_SOURCE
#include <stdlib.h>
#include <string.h>
#include <stdio.h>


#define MAX_LINES 1000

char *lines[MAX_LINES];
int   num_lines;


int compare(const void *s, const void *t)
{
    return strcmp(*(char **)s, *(char **)t);
}


int main(int argc, char *argv[])
{
    int i;
    FILE *infile;
    char *buffer;

    /* size_t is really another name for an int, but using
     * this silences a compiler warning when using getline().
     */
    size_t buffer_len = 0;


    if (argc < 2) {
        fprintf(stderr, "usage: %s <filename>\n", argv[0]);
        exit(1);
    }

    infile = fopen(argv[1], "r");
    if (infile == NULL) {
        fprintf(stderr, "%s: cannot open %s\n", argv[0], argv[1]);
        exit(1);
    }

    for (i = 0; i < MAX_LINES; i++) {
        lines[i] = NULL;
    }

    num_lines = 0;
    buffer = NULL;

    // HINT: Use getline()
    while(getline(&buffer, &buffer_len, infile) != -1) {
        size_t len = strlen(buffer);
        if(len > 0 && buffer[len -1] == '\n') {
            buffer[len - 1] = '\0';
        }

        lines[num_lines] = (char *) malloc(len + 1);
        if(lines[num_lines] == NULL) {
            fprintf(stderr, "Failed\n");
            exit(1);
        }
        strcpy(lines[num_lines], buffer);
        num_lines++;
    }

    fclose(infile);
    
    qsort(lines, num_lines, sizeof(char *), compare);

    for(i = 0; i < num_lines; i++) {
        printf("%s\n", lines[i]);
    }

    for(i = 0; i < num_lines; i++) {
        free(lines[i]);
    }

    free(buffer);
   
    return 0;
}
