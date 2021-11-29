
#include<iostream>
#include<stdio.h>
#include<vector>
using namespace std;

int main()
{
    int m=3,n=7;
    int arr[m][n];
    
    
    for(int i=0;i<1;i++)
    {
        for(int j=0;j<n;j++)
        {
            arr[i][j] = 1;
        }
    }
    
    
    for(int i=0;i<m;i++)
    {
        arr[i][0] = 1;
    }
    
    
    
    for(int i=1;i<m;i++)
    {
        for(int j=1;j<n;j++)
        {
            arr[i][j] = arr[i-1][j] + arr[i][j-1];
        }
        
    }
    
    
    
    //printing the 2d dp array
    for(int i=0;i<m;i++)
    {
        for(int j=0;j<n;j++)
        {
            cout<<arr[i][j];
        }
        
        cout<<"\n";
    }
    
    
    cout<<"\n"<<arr[m-1][n-1];
    return 0;
}
