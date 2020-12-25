#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    int a = 123456, b, c = 0;
    //cout << "enter you no: " << endl;
    //cin >> a;
    while (a > 0)
    {
        b = a % 10;
        a = a / 10;
        c = 10 * c + b;
        cout << c << endl;
    }
}