#include <stdio.h>
#include <stdlib.h>

int main() 
{
    FILE *fptr;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;

   if ((fptr = fopen("/Users/anna/Documents/AoC\ 2023/input1.txt","r")) == NULL){
       printf("Error! opening file");

       // Program exits if the file pointer returns NULL.
       exit(1);
   }

     while ((read = getline(&line, &len, fptr)) != -1) {
        printf("Retrieved line of length %zu:\n", read);
        printf("%s", line);
    }

    fclose(fptr);



    return 0;
}