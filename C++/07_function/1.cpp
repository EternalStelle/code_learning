#include <iostream>
void simple(); // 函数原型

int main()
{
    using namespace std;
    cout << "main() will call the simple function:\n";
    simple(); // 函数调用
    cout << "main() is finished with the simple() function";
    return 0;
}

void simple() // 函数定义
{
    using namespace std;
    cout << "I'm but a simple function.\n";
}