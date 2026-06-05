#include <stdio.h>

void meow(void){
    printf("meow\n");
}

int main(void)
{
    int user_input;
    do
    {
        printf("Enter a number: ");
        scanf("%d", &user_input);
    }
    while (user_input < 1);

    int iterations = user_input;
    for (int i = 0; i < iterations; i += 1){
        printf("Iteration: %d\n", i + 1);
        meow();
    }

    char Exit;
    do
    {
    printf("Press e and space to exit... ");
    scanf(" %c", &Exit);
    }
    while ( Exit != 'e');
    return 0;
}