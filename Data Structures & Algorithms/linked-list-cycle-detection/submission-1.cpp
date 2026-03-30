/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    bool hasCycle(ListNode* head) {
        std::unordered_set<ListNode*> set;  
        ListNode* ptr = head;

        while (ptr) {
           if (set.find(ptr) != set.end()) {
            return true;  
           } else {
            set.insert(ptr); 
            ptr = ptr->next; 
           } 
        } 
        return false; 

    }
};
