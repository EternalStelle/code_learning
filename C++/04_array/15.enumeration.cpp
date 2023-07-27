#include <iostream>
int main()
{
    using namespace std;
    //枚举enum，创建spectrum枚举变量
    enum spectrum {red, orange, yellow, blue, violet, indigo, ultraviolet};
    //创建band枚举变量
    spectrum band;
    //枚举变量只可被枚举量赋值
    band = blue;
    //可显式设置枚举值
    enum bits {one = 1, two = 2, four = 4, eight = 8};
    enum bigstep {first, second = 100, third};//此处third枚举值为101
}