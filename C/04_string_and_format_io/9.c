#include <stdio.h>
#define BLURB "Authentic imitation!"
int main(void)
{
    //要求为2，但自动扩大
    printf("[%2s]\n",BLURB);
    printf("[%24s]\n",BLURB);
    //精度为5，即只有5个字符
    printf("[%24.5s]\n",BLURB);
    //正值为右对齐，负值为左对齐
    printf("[%-24.5s]\n",BLURB);
    return 0;
}