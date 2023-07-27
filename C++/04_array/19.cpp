#include <iostream>
int main()
{
    using namespace std;
    int nights = 1001;
    // 使用new分配符合int的内存，其地址赋予指针pt
    int *pt = new int;
    *pt = 1001;

    cout << "nights value = ";
    cout << nights << ": location " << &nights << endl;
    cout << "int ";
    cout << "value = " << *pt << ": location = " << pt << endl;
    double *pd = new double;
    *pd = 10000001.0;

    cout << "double ";
    cout << "value = " << *pd << ": location = " << pd << endl;
    cout << "location of pointer pd: " << &pd << endl;
    cout << "size of pt = " << sizeof(pt);
    cout << ": size of *pt = " << sizeof(*pt) << endl;
    cout << "size of pd = " << sizeof(pd);
    cout << ": size of *pd = " << sizeof(*pd) << endl;

    // 使用delete释放用new分配的内存
    delete pt;
    delete pd;
    // 不可重复释放，也不可释放通过声明变量获得的内存，即
    /*
    int test;
    int * pt = &test;
    delete pt;
    是不允许的，delete仅用作释放new获得的内存
    */
    return 0;
}