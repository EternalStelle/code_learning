#include <iostream>
struct inflatable
{
    char name[20];
    float volume;
    double price;
};

int main()
{
    using namespace std;
    // 创建动态结构，令指针ps指向其
    inflatable *ps = new inflatable;
    cout << "Enter name of inflatable item: ";
    cin.get(ps->name, 20); // 使用ps->name调用结构中的name
    cout << "Enter volume in cubic feet: ";
    cin >> (*ps).volume; // 使用(*ps).volume调用结构中的volume，不适用句点运算符
    cout << "Enter price: $";
    cin >> ps->price;
    cout << "Name: " << (*ps).name << endl;
    cout << "Volume: " << ps->volume << endl;
    cout << "Price: $" << ps->price;
    delete ps;
    return 0;
}