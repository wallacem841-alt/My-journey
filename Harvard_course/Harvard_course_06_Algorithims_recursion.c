#include <stdio.h>

void draw(int n);
void draw_recursion(int n);
int main(void)
{
    int height = 4;

    draw(height);
    draw_recursion(height);
}

void draw(int n)
{
    for(int i = 0; i < n; i+=1)
    {
        for(int j = 0; j < i + 1; j+=1)
        {
            printf("#");
        }
        printf("\n");
    }
}
void draw_recursion(int n)
{
    if (n <= 0)
    {
        return;
    }
    draw_recursion(n-1);

    for(int i = 0; i < n; i+=1)
    {
        printf("#");
    }
    printf("\n");
}