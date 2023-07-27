#include <iostream>
void countdown(int n);
int main()
{
    countdown(4);
    return 0;
}

void countdown(int n)
{
    //函数递归调用，先由外到内，再由内到外
    using namespace std;
    cout << "Counting down ... " << n << endl;
    if (n > 0)
        countdown(n - 1);
    cout << n << ": Kaboom!\n";
}