// Time类使用与重载运算符
#include <iostream>
#include "mytime1.h"
#include "mytime1.cpp"

int main()
{
    using std::cout;
    using std::endl;
    Time planning;
    Time coding(2, 40);
    Time fixing(5, 55);
    Time total;

    cout << "planning time: ";
    planning.Show();
    cout << endl;

    cout << "coding time: ";
    coding.Show();
    cout << endl;

    cout << "fixing time: ";
    fixing.Show();
    cout << endl;

    total = coding + fixing;
    cout << "coding + fixing = ";
    total.Show();
    cout << endl;
    return 0;
}