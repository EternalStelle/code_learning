#include <iostream>
struct inflatable
{
    char name[20];
    float volume;
    double price;
};
/*可写作
struct inflatable
{
    char name[20];
    float volume;
    double price;
} bouquet, choice;
同时创建结构和结构变量
*/

int main()
{
    using namespace std;
    inflatable bouquet =
        {
            "sunflowers",
            0.20,
            12.49};
    inflatable choice;
    cout << "bouquet: " << bouquet.name << " for $";
    cout << bouquet.price << endl;
    // struct可赋值，只要结构相同
    choice = bouquet;
    cout << "choice: " << choice.name << " for $";
    cout << choice.price << endl;

    return 0;
}