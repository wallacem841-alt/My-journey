#include <stdio.h>

int main(void)
{
    int score_number;

    // Ask user for number of scores (no negative or zero scores)
    do
    {
        printf("How many scores?: ");
        scanf("%d", &score_number);
    }
    while (score_number < 1);

    int scores[score_number];

    // Input each score
    for (int i = 0; i < score_number; i += 1)
    {
        printf("What's score #%d?: ", i + 1);
        scanf("%d", &scores[i]);
    }

    int total_score = 0;

    // Calculate total score
    for (int i = 0; i < score_number; i += 1)
    {
        total_score += scores[i];
    }

    // Calculate and print average
    printf("The average score is: %.2f\n", (float) total_score / score_number);

    char exit_char;
    
    // Exit prompt
    do
    {
        printf("Press 'e' and Enter to exit... ");
        scanf(" %c", &exit_char);
    }
    while (exit_char != 'e');

    return 0;
}
