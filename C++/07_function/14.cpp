#include <iostream>
#include <string>
using namespace std;
const int SIZE = 5;
//string sa[]即为字符串数组，每个字符串即为一个数组元素
void display(const string sa[], int n);
int main()
{
    string list[SIZE];
    cout << "Enter your " << SIZE << " favourite astronomical sights:\n";
    for (int i = 0; i < SIZE; i++)
    {
        cout << i + 1 << ": ";
        getline(cin, list[i]);
    }
    cout << "Your list:\n";
    display(list, SIZE);
    return 0;
}

void display(const string sa[], int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << i + 1 << ": " << sa[i] << endl;
    }
}