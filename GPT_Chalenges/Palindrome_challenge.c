//Palindrome challenge
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int palindrome(char *input_word);
int main(void)
{
    char input_word[] = "raD:ar:";
    int pal_value = palindrome(input_word);
    printf("%i", pal_value);
}

int palindrome(char *input_word)
{
    int size_word = strlen(input_word);
 
    for (int i = 0; i < size_word; i+=1)
    {
        input_word[i] = tolower(input_word[i]);
    }

    for (int i = 0; i < size_word; i+=1)
    {
        if (isalnum(input_word[i]) == 0)
        {
            for (int j = i; input_word[j] != '\0'; j+=1)
            {
                input_word[j] = input_word[j + 1];
            }
            size_word -= 1;
        }
    }
    for (int i = 0; i < size_word/2; i+=1)
    {
        if (input_word[i] != input_word[size_word - (i+1)])
        {
            return 1;
        }
    }
    return 0;
}