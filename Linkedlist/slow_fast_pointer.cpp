class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        
        ListNode* fast = head;
        ListNode* slow = head;
        
        //using fast and slow pointer approach
        while(fast != NULL && fast->next != NULL)
        {
            fast = fast->next->next;
            slow = slow->next;
        }
        
        return slow;
    }
};
