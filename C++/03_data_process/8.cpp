#include <iostream>
int main()
{
    using namespace std;
    int auks, bats, coots;
    //将19.99和11.99视作double计算后取为int输出
    auks = 19.99 + 11.99;
    //先显式转换19.99和11.99为int，再做相加
    bats = (int) 19.99 + (int) 11.99;
    coots = int (19.99) + int (11.99);
    cout << "auks = " << auks << ",bats = " << bats;
    cout << ", coots = " << coots << endl;
    //可使用static_cast<>()来转换
    char ch = 'Z';
    cout << "The code for " << ch << " is ";
    cout << int(ch) << endl;
    cout << "Yes, the code is ";
    cout << static_cast<int>(ch) << endl;
    /*
    可利用auto自动将变量转换为与其相同的类型
    auto a = 0.1;
    auto b = 1;
    auto c = 1.3e12L;
    a即被定为double类型，b即被定为int类型，c即为long double类型
    */
    return 0;
}