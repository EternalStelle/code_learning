#include <iostream>
int main()
{
    using namespace std;
    cout.setf(ios_base::fixed, ios_base::floatfield);
    //整型除法不保留小数部分
    cout << "Interger division: 9/5 = " << 9/5 << endl;
    cout << "Floating-point division: 9.0/5.0 = ";
    //浮点数默认为double
    cout << 9.0/5.0 << endl;
    //不同类型的运算会自动转换为同一类型
    cout << "Mixed divosion: 9.0/5 = " << 9.0/5 << endl;
    //double和float的精度不同导致答案精度不同
    cout << "double constants: 1e7/9.0 = ";
    cout << 1.e7/9.0 << endl;
    cout << "float constants: 1e7f/9.0f = ";
    cout << 1.e7f/9.0f << endl;
    return 0;
}