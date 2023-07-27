#include <stdio.h>
int main(void)
{
    float weight;
    float value;
    printf("Are you worh your weight in platinum?\n");
    printf("Let's check it out.\n");
    printf("Please enter your weight in pounds: ");
    scanf("%f", &weight);
    value = 1700.0 * weight * 14.5833;
    printf("Your weight in platnium is worth $%.2f.\n", value);
    printf("You are easily worth that!");
    return 0;
}