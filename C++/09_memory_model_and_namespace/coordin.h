//头文件仅包含一个，故#ifndef和#endif用于确保编译时若无COORDIN_H_再编译此文件，防止冲突
#ifndef COORDIN_H_
#define COORDIN_H_

struct polar
{
    double distance;
    double angle;
};

struct rect
{
    double x;
    double y;
};

polar rect_to_polar(rect xypos);
void show_polar(polar dapos);

#endif