/* Two sum Pairs Using Map in C++, we keep the index and element as key-value pairs*/

#include<iostream>
#include <stdio.h>
#include<vector>
#include<map>
using namespace std;

int main()
{
    vector<int> vect{2,7,11,5};
    int target = 9;
    
    vector<int> pair;
    map<int, int> ele;
    
    for(int i=0;i<vect.size();i++)
    {
        if(ele.count(target-vect[i]))
        {
            pair.push_back(ele[target-vect[i]]);
            pair.push_back(i);
            break;
        }
        
        ele[vect[i]] = i;

    }
    
    for(auto k:pair)
    {
        cout<<k;
    }
    

    return 0;
}
