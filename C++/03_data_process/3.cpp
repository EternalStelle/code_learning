#include <iostream>
using namespace std;
int main()
{
    char ch;
    cout << "Enter a character: " << endl;
    cin >> ch;
    cout << "Thank you for " << ch << " in input" << endl;
    int i = ch;
    cout << ch << "的ASCII码为：" << i << endl;
    ch = ch + 1;
    i = ch;
    cout << "下一个符号为：" << ch << "，对应的ASCII码为：" << i << endl;
    cout << "使用cout.put()输出字符" << endl;
    cout.put(ch);
    cout.put('!');
    return 0;
}