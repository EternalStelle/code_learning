#include <stdio.h>
#include <string.h>
#define DENSITY 62.4
int main(void)
{
    float weight,volume;
    int size, letters;
    char name[40];
    printf("Enter your name: ");
    scanf("%s", name);
    printf("%s, Enter your weight in pounds: ",name);
    scanf("%f", &weight);
    size = sizeof(name);
    letters = strlen(name);
    volume = weight/DENSITY;
    printf("Well,%s,your volume is %2.2f cubic feet.\n", name, volume);
    printf("Als, your first name has %d letters,\n",letters);
    printf("and we have %d bytes to store it.\n",size);
    return 0;
}