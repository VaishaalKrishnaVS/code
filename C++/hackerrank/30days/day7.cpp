#include <iostream>
using namespace std;

int main()
{
    int n = 0;
    cin >> n;
    int C[n];
    for (int i = 0; i < n; i++)
    {
        cin >> C[i]; //user definable array
    }
    for (int i = n - 1; i >= 0; i--)
    {
        cout << C[i] << " ";
    }
}
