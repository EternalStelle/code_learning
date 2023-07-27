#include <iostream>
int main()
{
    using namespace std;
    int higgens = 5;
    // 使用&获得地址，直接初始化指针
    int *pt = &higgens;

    cout << "Value of higgens = " << higgens
         << "; Address of higgens = " << &higgens << endl;
    cout << "Value of *pt = " << *pt
         << "; Value of pt = " << pt << endl;

    // pt = (int *) 0xB8000000;可使用此种方法直接赋予指针地址，必须有(int *)以使类型(地址)匹配
    return 0;
}