#include <stdio.h>
int main(void)
{
    //十六进制输出，加#可输出0x格式，大小写x决定输出大小写法
    printf("%x**%X**%#x\n", 31, 31, 31);
    printf("**%d**%d**%d**\n", 42, 42, -42);
    //若0与.精度要求同时出现，0标记被忽略
    printf("**%5d**%5.3d**%05d**%05.3d**\n", 6, 6, 6, 6);
    return 0;
}