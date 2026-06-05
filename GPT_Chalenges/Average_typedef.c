#include <stdio.h>

typedef struct 
{
    int id;
    float gpa;
} Student;

int main(void)
{
    Student students[] =
    {
        {1, 3.5},
        {2, 3.8},
        {3, 4.0},
        {4, 2.8}
    };
    int size = sizeof(students)/sizeof(students[0]);
    float total = 0;
    for(int i = 0; i < size; i+=1)
    {
        total += students[i].gpa;
    }
    printf("%.2f", total/size);
}