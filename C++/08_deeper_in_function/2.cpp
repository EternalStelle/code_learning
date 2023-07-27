//引用变量可把某个变量作为另一变量的别名
//它们的地址与内容相同，可使函数使用其原始内容，可充当指针的功能
#include <iostream>
int main()
{
    using namespace std;
    int rats=101;
    //令redents为rats的别名
    int & rodents = rats;
    cout << "rats = " <<rats;
    cout << ", redents = " << rodents<< endl;
    rodents++;
    cout << "rats = " <<rats;
    cout << ", redents = " << rodents<<endl;

    cout << "rats address = " <<&rats;
    cout << ", redents address = " << &rodents <<endl;
    return 0;
}