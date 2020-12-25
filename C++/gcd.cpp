#include <iostream>
using namespace std;

int main()
{
    int m = 12, n = 15;
    //cout << "enter two nos: ";
    //cin >> m >> n;

    while (m != n)
    {
        if (m > n)
        {
            m = m - n;
        }
        else if (n > m)
        {
            n = n - m;
        }
    }
    cout << m;
}