#include <stdio.h>
int main(void)
{
    float aboat = 32000.0;
    double abet = 2.14e9;
    long double dip = 5.32e-5;
    printf("%f can be written %e\n", aboat,aboat);
    //%a为十六进制e指数形式输出
    printf("And it's %a in hexadecimal format, powers of two notations\n", aboat);
    //%e即为e指数形式输出
    printf("%f can be written %e\n", abet,abet);
    printf("%Lf can be written %Le\n",dip,dip);
    return 0;
}