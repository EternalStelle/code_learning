#include <iostream>
struct widget
{
    char brand[20];
    int type;
    //union共用体，不可同时调度不同类型数据，使用id_num时id_char丢失数据，反之亦然
    union id
    {
        long id_num;
        char id_char[20];
    } id_val;
};

int main()
{
    using namespace std;
    widget prize;
    if (prize.type == 1)
        cin >> prize.id_val.id_num;
    else
        cin >> prize.id_val.id_char;
    return 0;
}