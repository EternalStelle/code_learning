#include <iostream>
#include <ctime>
int main()
{
    using namespace std;
    cout << "Enter the delay time, in seconds: ";
    float secs;
    cin >> secs;
    clock_t delay = secs * CLOCKS_PER_SEC;//把秒数转换为系统ticks
    cout << "starting\a\n";
    clock_t start = clock();//令start与系统初始时间一致
    while (clock() - start < delay)//当系统时间与start代表的初始时间之差(延迟)小于delay时离开循环体
    {
        ;
    }
    cout << "done.\a\n";
    return 0;
}