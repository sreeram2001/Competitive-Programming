/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        
        ListNode* node = head;
        
        if(head == NULL)
        {
            return NULL;
        }
        
        while(node->next != NULL)
        {
            node->val = NULL;
    
            if(node->next->val == NULL)
            {
                return node->next;
            }
            node = node->next;
        }
        
        return NULL;
    }
};
