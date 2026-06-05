#include <stdio.h>

int factorial_calc(int base);

int main(void)
{
    int factorial = 5;
    int result = factorial_calc(factorial);
    printf("%d", result);
}

int factorial_calc(int base)
{
    if (base <= 1)
    {
        return 1;
    }
    return base * factorial_calc(base - 1);
}