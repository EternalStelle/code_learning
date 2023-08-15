// 类声明
#ifndef MYTIME1_H_
#define MYTIME1_H_
class Time
{
private:
    int hours;
    int minutes;

public:
    Time();
    Time(int h, int m = 0);
    void AddMin(int m);
    void AddHr(int h);
    void Reset(int h = 0, int m = 0);
    // 重载+运算符
    Time operator+(const Time &t) const;
    // Time Sum(const Time &t) const;
    void Show() const;
};
#endif