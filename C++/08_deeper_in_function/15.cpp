#include <iostream>

template <typename T>
T lesser(T a,T b)
{
    return a < b ? a : b;
}
//可手动制定转换规则，当输入输出均为int时采用制定的函数，而不是模板生成
int lesser(int a,int b)
{
    a = a < 0 ? -a : a;
    b = b < 0 ? -b : b;
    return a < b ? a : b;
}

int main()
{
    using namespace std;
    int m = 20;
    int n = -30;
    double x = 15.5;
    double y = 25.9;

    cout << lesser(m, n) << endl;
    cout << lesser(x, y) << endl;
    //其中的<>即指定模板函数，其中的int即代表强制转换为int
    cout << lesser<>(m, n) << endl;
    //显式实例化为int
    cout << lesser<int>(x, y) << endl;
    return 0;
}