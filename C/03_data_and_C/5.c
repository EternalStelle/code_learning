#include <stdio.h>
int main(void)
{
    //sizeof()用于显示类型大小，%zd为专用类型，可用%u或%ul
    printf("Type int has size of %zd bytes\n", sizeof(int));
    printf("Type char has size of %zd bytes\n", sizeof(char));
    printf("Type long has size of %zd bytes\n", sizeof(long));
    printf("Type long long has size of %zd bytes\n", sizeof(long long));
    printf("Type double has size of %zd bytes\n", sizeof(double));
    printf("Type long double has size of %zd bytes\n", sizeof(long double));
    return 0;
}