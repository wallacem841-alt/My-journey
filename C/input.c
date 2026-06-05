#include <stdio.h>

int main() {
    int number;
    float decimal;
    char c;
    
    printf("Enter an integer: ");
    scanf("%d", &number);
    
    printf("Enter a float: ");
    scanf("%f", &decimal);
    
    printf("You entered %d and %.2f\n", number, decimal);

    printf("Press enter to exit...");
    c = getchar(); // Get a single character
    getchar();
    return 0;
}
