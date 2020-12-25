#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    int a = 153, b, c = 0;
    //cout << "enter you no: " << endl;
    //cin >> a;
    int m = a;
    while (a > 0)
    {
        b = a % 10;
        a = a / 10;
        c += pow(b, 3);
    }
    if (c == m)
    {
        cout << "it is an amstrong number" << endl;
    }
    else
    {
        cout << "it is not an amstrong number" << endl;
    }
}