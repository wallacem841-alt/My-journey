#include <stdio.h>

int is_prime(int n);

int backtrack(int n, int temp);

int main(void)
{
    int x = 523;
    int result = is_prime(x);
    printf("%d", result);
}

int is_prime(int n)
{
    if (n <= 1)
    {
        return 2;
    }
    else if (n == 2)
    {
        return 1;
    }

    int temp = n;

    return backtrack(n, temp);
}

int backtrack(int n, int temp)
{
    if (n == 2)
    {
        return 1;
    }

    if (temp % (n-1) == 0)
    {
        return 0;
    }

    return backtrack(n - 1, temp);
}