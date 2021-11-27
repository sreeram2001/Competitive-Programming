
#include<iostream>
#include <stdio.h>
#include<vector>
using namespace std;
#include <bits/stdc++.h>

int main()
{
    int a[5] = {0, 2, 1, 2, 0};
    int n = 5;
    
    int zero = count(a,a+n,0);
    int one = count(a,a+n,1);
    int two = count(a,a+n,2);
    
    int i=0;
    int j=zero;
    int k = j+one;
    
    for(int i=0;i<zero;i++)
    {
        a[i] = 0;
    }
    
    for(int i=j;i<j+one;i++)
    {
        a[i] = 1;
    }
    
    
    for(int i=k;i<k+two;i++)
    {
        a[i] = 2;
    }
    
    for(int i=0;i<n;i++)
    {
        cout<<a[i];
    }

    return 0;
}
