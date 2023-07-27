#include <iostream>
#include <string>
// 声明结构，此处为外部声明，可被文件中的任意函数使用，在main中则不是
struct inflatable
{
    char name[20];
    // 也可使用std::string name;把string用在声明中(可把using调至结构声明前，直接写string name)
    float volume;
    double price;
};

int main()
{
    using namespace std;
    inflatable guest =
        {
            "Glorious Gloria",
            1.88,
            29.99};
    // 也可写作inflatable guest = {"Glorious Gloria", 1.88, 29.99};(等号可有可无)
    inflatable pal =
        {
            "Audacious Arthur",
            3.12,
            32.99};

    cout << "Expand your guest list with " << guest.name;
    cout << " and " << pal.name << "!\n";
    cout << "You can have both for $";
    cout << guest.price + pal.price << ".\n";
    return 0;
}