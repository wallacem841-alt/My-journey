#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int number;
    struct node *next;
} node;

int main(void) {
    // Predefined list of numbers
    int numbers[] = {10, 20, 30, 40, 50};
    int numCount = sizeof(numbers) / sizeof(numbers[0]);

    // Memory for numbers
    node *list = NULL;

    // Add numbers to the linked list
    for (int i = 0; i < numCount; i++) {
        // Allocate node for number
        node *n = malloc(sizeof(node));
        if (n == NULL) {
            return 1;
        }
        n->number = numbers[i];
        n->next = NULL;

        // Prepend node to list
        n->next = list;
        list = n;
    }

    // Print numbers
    node *ptr = list;
    while (ptr != NULL) {
        printf("%i\n", ptr->number);
        ptr = ptr->next;
    }

    // Free memory
    ptr = list;
    while (ptr != NULL) {
        node *next = ptr->next;
        free(ptr);
        ptr = next;
    }

    return 0;
}