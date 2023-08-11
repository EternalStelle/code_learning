//提供类定义
//使用#ifndef...#endif防止重复定义
#ifndef STOCK10_H
#define STOCK10_H
#include <string>

class Stock
{
    private:
        std::string company;
        long shares;
        double share_val;
        double total_val;
        void set_tot() { total_val = shares * share_val; }
    public:
        Stock();//构造函数
        Stock(const std::string &co, long n = 0, double pr = 0.0);
        ~Stock();//析构函数
        void buy(long num, double price);
        void sell(long num, double price);
        void update(double price);
        void show();
};

#endif