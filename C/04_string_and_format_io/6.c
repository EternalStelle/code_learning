#include <stdio.h>
#define PAGES 959
int main(void)
{
    printf("*%d*\n",PAGES);
    printf("*%2d*\n",PAGES);
    //%10d即令输出有10个字符宽度
    //正数即为右对齐，负数为左对齐
    printf("*%10d*\n",PAGES);
    printf("*%-10d*\n",PAGES);
    return 0;
}