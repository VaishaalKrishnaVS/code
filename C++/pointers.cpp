#include <iostream>
using namespace std;

int main()
{
    int x = 10;
    int *p; // declaration
    p = &x; // intialization
    cout << x << endl;
    cout << &x << endl;
    cout << p << endl;
    cout << &p << endl;
    cout << *p << endl; // dereferencing
}