#include <stdio.h>

typedef struct 
{
    int id;
    float gpa;
} Student;

float average_calc(Student students[], int size);
float sum_students(Student students[], int size);

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

    float result = average_calc(students, size);
    printf("%.2f", result);
}

float average_calc(Student students[], int size)
{
    float total = sum_students(students, size);
    return total/size;
}

float sum_students(Student students[], int size)
{
        if (size <= 0)
    {
        return 0;
    }
    return students[size - 1].gpa + sum_students(students, size - 1);
}