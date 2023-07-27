#include <iostream>
#include <cmath>
int main(void)
{
    using namespace std;
    double area;
    cout << "Enter the floor area (in square metre) of your house:";
    cin >> area;
    double side;
    //使用sqrt()应预处理文件cmath
    side = sqrt(area);
    cout << "That's " << side << " metre." <<endl;
    cout << "That's the side of your house!" << endl;
    return 0;
}