#include <iostream>
//函数模版，可用于重复生成功能相同，量不同的函数
template <typename T>
void Swap(T &a, T &b);
int main()
{
    using namespace std;
    int i = 10;
    int j = 20;
    cout << "i, j = " << i << ", " << j << ".\n";
    cout << "Using compliler-generated int swapper:\n";
    Swap(i, j);
    cout << "Now i, j = " << i << ", " << j << endl;

    double x = 24.5;
    double y = 81.7;
    cout << "x, y = " << x << ", " << y << ".\n";
    cout << "Using compliler-generated int swapper:\n";
    Swap(x, y);
    cout << "Now x, y = " << x << ", " << y << endl;
    return 0;
}

template <typename T>
void Swap(T &a, T &b)
{
    T temp;
    temp = a;
    a = b;
    b = temp;
}