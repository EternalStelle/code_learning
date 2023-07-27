#include <iostream>
double cube(double a);
double refcube(double &ra);
int main()
{
    using namespace std;
    double x = 3.0;
//按值传递，不修改原值
    cout << cube(x);
    cout << " = cube of " << x << endl;
//引用传递会修改原值，且此处有创建临时变量
    cout << refcube(x);
    cout << " = cube of " << x << endl;

    return 0;
}

double cube(double a)
{
    a *= a * a;
    return a;
}

double refcube(double &ra)
{
    ra *= ra * ra;
    return ra;
}