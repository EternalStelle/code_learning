#include <iostream>
extern double warming;

void update(double dt);
void local();

using std::cout;
void update(double dt)
{
    //该声明为可选，仅为表明使用的是外部变量
    extern double warming;
    warming += dt;
    cout << "Updating global warming to " << warming;
    cout << " degrees.\n";
}

void local()
{
    double warming = 0.8;
    cout << "Local warming = " << warming << " degrees.\n";
    //::运算符表明采用变量的全局版本
    cout << "But global warming = " << ::warming;
    cout << " degrees.\n";
}