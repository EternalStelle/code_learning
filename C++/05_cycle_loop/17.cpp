#include <iostream>
int main()
{
    using namespace std;
    char ch;
    int count = 0;
    cin.get(ch);
    while (cin.fail() == false)//亦可写作while(!cin.fail())或while(cin)
    {
        cout << ch;
        ++count;
        cin.get(ch);
    }
    cout << endl << count << " charaters read.\n";
    return 0;
}