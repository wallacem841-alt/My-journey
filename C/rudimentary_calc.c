#include <stdio.h>

int main(void) {
    char check = ' ';  // Initialize check with a non-'e' character
    while (check != 'e') {
        int x, y = 0;
        char operando;

        printf("Enter an integer: ");
        scanf("%d", &x);

        printf("Enter another integer: ");
        scanf("%d", &y);

        printf("Choose the operator (/, *, -, +): ");
        scanf(" %c", &operando);  // Use & to pass the address

        if (operando == '/') {
            if (y != 0) {
                printf("Division result: %d\n", x / y);
            } else {
                printf("Error: Division by zero!\n");
            }
        } else if (operando == '*') {
            printf("Multiplication result: %d\n", x * y);
        } else if (operando == '-') {
            printf("Subtraction result: %d\n", x - y);
        } else if (operando == '+') {
            printf("Sum result: %d\n", x + y);
        } else {
            printf("Choose a valid operator.\n");
        }

        printf("Press 'e' to exit or any other key to repeat: ");
        scanf(" %c", &check);  // Use & to pass the address
    }

    printf("Calculator exited. Goodbye!\n");
    return 0;
}