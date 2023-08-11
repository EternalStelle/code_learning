//提供类定义
//使用#ifndef...#endif防止重复定义
#ifndef STOCK20_H
#define STOCK20_H
#include <string>

class Stock
{
    private:
        std::string company;
        int shares;
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
        void show()const;
        const Stock &topval(const Stock &s) const;
        //括号后的()表示函数不对被隐式调用的对象进行修改
};

#endif