#include <iostream>
int main()
{
    using namespace std;
    double *p3 = new double[3];
    p3[0] = 0.2;
    p3[1] = 0.5;
    p3[2] = 0.8;
    cout << "p3[1] is " << p3[1] << ".\n";
    // 指针加一即变为下一个元素的地址
    p3 = p3 + 1;
    cout << "Now p3[0] is " << p3[0] << " and ";
    cout << "p3[1] is " << p3[1] << ".\n";
    // 指针减一即变为前一个元素的地址
    p3 = p3 - 1;
    delete[] p3;
    return 0;
}