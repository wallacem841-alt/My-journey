#include <stdio.h>
#include <ctype.h>
#include <string.h>

void preprocess(char *input_word);
int is_palindrome_recursive(char *input_word, int left, int right);

int main(void)
{
    char input_word[] = "RaD:ar:"; // Test with mixed case
    preprocess(input_word);
    
    int pal_value = is_palindrome_recursive(input_word, 0, strlen(input_word) - 1);
    printf("%i\n", pal_value); // Output 0 for palindrome, 1 for not
}

// Preprocess the string to lowercase and remove non-alphanumeric characters
void preprocess(char *input_word)
{
    int size_word = strlen(input_word);
    int j = 0; // Pointer for the new position in the array

    for (int i = 0; i < size_word; i += 1)
    {
        input_word[i] = tolower(input_word[i]); // Convert to lowercase

        // Only copy alphanumeric characters
        if (isalnum(input_word[i]))
        {
            input_word[j] = input_word[i];
            j += 1;
        }
    }
    input_word[j] = '\0'; // Null-terminate the new string
}

// Recursive function to check if the string is a palindrome
int is_palindrome_recursive(char *input_word, int left, int right)
{
    if (left >= right) // Base case: all characters checked
    {
        return 0; // Is a palindrome
    }
    if (input_word[left] != input_word[right]) // Check characters
    {
        return 1; // Not a palindrome
    }
    
    return is_palindrome_recursive(input_word, left + 1, right - 1); // Recur for the next pair
}
