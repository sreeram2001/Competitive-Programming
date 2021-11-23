/*  Question : Given an array arr[] denoting heights of N towers and a positive integer K, 
you have to modify the height of each tower either by increasing or decreasing them by K only once. 
After modifying, height should be a non-negative integer. 
Find out what could be the possible minimum difference of the height of shortest and 
longest towers after you have modified each tower.*/

/* geeks for geeks => Minimize the Heights - II*/


#include<stdio.h>
#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
    vector<int> arr{1, 8, 5, 10};
    int k = 2;
    int n = arr.size()-1;
    
    sort(arr.begin(),arr.end());            //sort the array initially
    
    int mini = arr[0] + k;  
    int maxi = arr[n] - k;                  //making index - 0 to increase and last index to decrease
    
    int ans = maxi - mini;                  //initially consider their difference as minimum difference b/w heights
    
    for(int i=0;i<n-1;i++)
    {
        mini = min(mini,arr[i+1]-k);        //iterate thru each element, find minimum value by decreasing by k
        maxi = max(maxi,arr[i]+k);         //iterate thru each element, find max value by increasing by k 
        
        if(mini>0)
        {
            ans = min(ans,maxi-mini);       //update final ans only if minimum value > 0, else the difference will be large
        }
    }
    
    cout<<"OUTPUT : "<<ans;
    
    return 0;
}
