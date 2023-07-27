// 内联函数把函数定义放于原本函数原型的地方
// 可加速函数运行，但增加占用内存
#include <iostream>
//内联函数分号位于花括号内，其本质是把花括号内容替代入main函数中
inline double square(double x) { return x * x; }

int main()
{
    using namespace std;
    double a, b;
    double c = 13.0;
    a = square(5.0);
    b = square(4.5 + 7.5);
    cout << "a = " << a << ", b = " << b << endl;
    cout << "c = " << c;
    cout << ", c squared = " << square(c++) << "\n";
    cout << "Now c = " << c << endl;
    return 0;
}