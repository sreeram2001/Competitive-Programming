#include<iostream>
#include<stdio.h>
#include<vector>
using namespace std;

int maxi(vector<int> &arr, int k, int l)
{
    int window=0, maxi=0;
    
    for(int i=0;i<k;i++)
    {
        window = window + arr[i];
    }
    
    for(int i=0;i<l-k;i++)
    {
        window = window - arr[i] + arr[i+k];
    }
    
    return window;
}


int main()
{
    vector<int> arr = {1, 4, 2, 10, 2, 3, 1, 0, 20};
    int k = 4;
    int l = arr.size();
    int op = maxi(arr,k,l);
    
    cout<<op;
    return 0;
}
