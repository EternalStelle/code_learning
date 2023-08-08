#include <stdio.h>
int main(void)
{
    const double RENT = 3852.99;
    printf("*%f*\n", RENT);
    printf("*%e*\n", RENT);
    //4.2f即小数点左4位，.2即小数点右2位
    printf("*%4.2f*\n", RENT);
    printf("*%3.1f*\n", RENT);
    printf("*%10.3f*\n", RENT);
    //E即为E输出
    printf("*%10.3E*\n", RENT);
    //+号可令正数使用+在前输出，负数为-
    printf("*%+4.2f*\n", RENT);
    //0在前可令0填充不足的位数
    printf("*%010.2f*\n", RENT);
    return 0;
}