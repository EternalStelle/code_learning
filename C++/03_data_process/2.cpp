#include <iostream>
using namespace std;
int main()
{
    int a = 42;
    cout << "42在十进制下表示为：" << a << endl;
    //使用cout << hex或oct或dec可更改输出数的进制
    cout << hex;
    cout << "42在十六进制下表示为：" << a << endl;
    cout << oct;
    cout << "42在八进制下表示为：" << a << endl;
    return 0;
}