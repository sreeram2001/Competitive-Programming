class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        it = sum(tickets)
        count = 0
        total_time = [0 for i in range(len(tickets))]
        
        
        while it > 0:
            for i in range(len(tickets)):
                
                if tickets[i] > 0:
                    it = it - 1
                    count = count + 1
                    tickets[i] = tickets[i] - 1
                    
                    total_time[i] = count
        
        return total_time[k]
