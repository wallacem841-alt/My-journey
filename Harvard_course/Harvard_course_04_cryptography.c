#include <stdio.h>

int main(void){
    unsigned char user_input[21];
    int pi_digits[20] = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4};

    printf("Enter a word: ");
    scanf("%20s", user_input);  // Use %s to read a word, limit to 20 characters to avoid overflow

    // Clear the remaining input buffer in case of overflow
    while (getchar() != '\n');

    printf("Your protected message\n");
    for (int i = 0; i < 20 && user_input[i] != '\0'; i += 1){
        printf("%c", user_input[i] + pi_digits[i]);
    }
    printf("\n");
    char check;
    printf("Press any key and enter to exit: ");
    scanf(" %c", &check);  // Use & to pass the address
    return 0;
}