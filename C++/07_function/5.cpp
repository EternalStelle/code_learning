#include <iostream>
const int ArSize = 8;
int sum_arr(int arr[], int n);//此处arr[]为指针，而非数组
int main()
{
    using namespace std;
    int cookies[ArSize] = {1, 2, 4, 8, 16, 32, 64, 128};
    int sum = sum_arr(cookies, ArSize);
    cout << "Total cookies eaten: " << sum << endl;
    return 0;
}

int sum_arr(int arr[], int n)
{
    int total = 0;
    for (int i = 0; i < n; i++)
    {
        total = total + arr[i];//arr[i]也即*(arr+i)
    }
    return total;
}