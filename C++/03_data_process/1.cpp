#include <iostream>
#include <climits>
int main()
{
    using namespace std;
    int n_int = INT_MAX;
    short n_short = SHRT_MAX;
    long n_long = LONG_MAX;
    unsigned long long n_llong = ULLONG_MAX;

    cout << "int有" << sizeof(int) << "个字节" << endl;
    cout << "short有" << sizeof(n_short) << "个字节" << endl;
    cout << "long有" << sizeof(long) << "个字节" << endl;
    cout << "unsigned long long有" << sizeof(n_llong) << "个字节" << endl;

    cout << "int输出最大值：" << n_int << endl;
    cout << "unsigned short输出最大值：" << n_short << endl;
    cout << "long输出最大值：" << n_long << endl;
    cout << "unsigned long long输出最大值：" << n_llong << endl;

    cout << "int最小值为：" << INT_MIN <<endl;
    cout << "每字节有" << CHAR_BIT << "比特" << endl;

    return 0;
}