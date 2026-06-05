#include <stdio.h>

void reverse_string(char str[], int start, int end);

int main(void)
{
    char string[] = "Banana";
    int length = sizeof(string)/sizeof(string[0]);
    reverse_string(string, 0, length - 2);
    printf("%s\n", string);
    
    char reversed_string[length - 1];
    for (int i = length - 2, j = 0; i >= 0; i-=1, j += 1)
    {
        reversed_string[i] = string[j];
    }
    reversed_string[length - 1] = '\0';
    printf("%s\n", reversed_string);


}

void reverse_string(char str[], int start, int end) {
    if (start >= end) {
        return; // Base case: when start meets or passes end
    }
    
    // Swap characters at start and end
    char temp = str[start];
    str[start] = str[end];
    str[end] = temp;
    
    // Move towards the center
    reverse_string(str, start + 1, end - 1);
}
