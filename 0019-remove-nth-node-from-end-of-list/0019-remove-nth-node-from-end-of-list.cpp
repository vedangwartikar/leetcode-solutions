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
    int count = 0;
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (head->next == NULL)
            return NULL;
        ListNode* temp = head;
        while (temp != NULL) {
            count += 1;
            temp = temp->next;
        }
        
        if (count == n)
            return head->next;
        
        temp = head;
        for (int i = 0; i < count - n - 1; i++) {
            cout << temp->val;
            temp = temp->next;
        }
        cout << temp->val;
        if (temp->next != NULL)
            temp->next = temp->next->next;
        return head;
    }
};