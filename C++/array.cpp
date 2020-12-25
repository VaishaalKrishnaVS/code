//ARRAY
#include <iostream>
using namespace std;

int main()
{
    char A[] = {81, 82, 88, 86, 83, 84, 85, 85, 88};
    for (char x : A) //for each loop
    {
        cout << x << endl;
    }

    int B[] = {81, 82, 88, 96, 83, 65, 80, 85, 89};
    int sum = 0;
    int max = B[0];
    int min = B[0];

    for (auto x : B)
    {
        if (x > max)
        {
            max = x;
        }
        if (x < min)
        {
            min = x;
        }

        sum += x;
        cout << x << endl;
        cout << sum << endl;                      //sum of array elements
        cout << max << " is the gratest" << endl; //max of array elements
        cout << min << " is the least" << endl;   //min of array elements
    }

    // LINEAR SEARCH

    int C[6] = {51, 75, 56, 6, 64, 46};
    //int C[6];
    int random_num = 56;
    //cout << "enter the nos :" << endl;
    //for (int i = 0; i < 6; i++)
    //{
    //     cin >> C[i];                                           //user definable array
    //}
    //cout<<"enter the random_no : "<<endl;
    //cin>>random_no;

    for (int i = 0; i < 6; i++)
    {
        if (random_num == C[i])
        {
            cout << i << endl;
            return 0;
        }
    }
}