#include <stdio.h>
#define PRAISE "You are an extraordinary being."

int main(void)
{
    char name[40];
    printf("Enter your name: ");
    scanf("%s", name);
    printf("Hello,%s.%s\n",name,PRAISE);
    return 0;
}