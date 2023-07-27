#include <iostream>
int main()
{
    using namespace std;
    for (int i = 0; i < 5; i++)
    //也可用如下写法，C语言仅有如下写法
    //int i;
    //for (i = 0; i < 5; i++)
    {
        cout << "C++ knows loops.\n";
    }
    cout << "C++ knows when to stop.\n";
    return 0;
}