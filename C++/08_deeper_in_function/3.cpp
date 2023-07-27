#include <iostream>
int main()
{
    using namespace std;
    int rats=101;
    //引用要在创建时即确定，并始终不变
    int & rodents = rats;

    cout << "rats = " <<rats;
    cout << ", rodents = " <<rodents << endl;
    
    cout << "rats address = " << &rats;
    cout << ", rodents address = " << &rodents<<endl;

    int bunnies=50;
    rodents =bunnies;
    cout << "bunnies = "<<bunnies;
    cout << ", rats = " <<rats;
    cout << ", rodents = " <<rodents<<endl;

    cout << "bunnies address = " <<&bunnies;
    cout <<", rodents address = " <<&rodents;

    return 0;
}