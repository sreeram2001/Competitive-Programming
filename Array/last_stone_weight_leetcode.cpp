class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        
        priority_queue<int> q;
        int maxi1, maxi2;
        
        for(int i=0;i<stones.size();i++)
        {
            q.push(stones[i]);
        }
        
        //heap queue push
        while(q.size() > 1)
        {
            maxi1 = q.top();
            q.pop();
            
            maxi2 = q.top();
            q.pop();
            
            if(maxi1 != maxi2)
            {
                q.push(maxi1 - maxi2);
            }
        }
        
        if(q.size() > 0)
        {
            return q.top();
        }
        else
        {
            return 0;
        }
    }
};
