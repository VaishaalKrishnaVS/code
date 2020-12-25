#include <iostream>
using namespace std;

int main()
{
    int A[10] = {21, 31, 51, 91, 105, 427, 481, 501, 620, 623};
    int lower = 0, higher = 9, middle;
    int random_no = 427;
    //cout<<"enter the no :"<<endl;
    //cin>>"random_no :";

    while (lower <= higher)
    {
        middle = (lower + higher) / 2;

        if (random_no == A[middle])
        {
            cout << "the number is psitioned at " << middle << endl;
            return 0;
        }
        else if (random_no > A[middle])
        {
            lower = middle + 1;
        }
        else
        {
            higher = middle - 1;
        }
    }
}