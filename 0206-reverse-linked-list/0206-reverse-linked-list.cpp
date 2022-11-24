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
    ListNode* reverseList(ListNode* head) {
        ListNode *new_node = NULL, *next_node = NULL;
        while (head) {
            next_node = head->next;
            head->next = new_node;
            new_node = head;
            head = next_node;
        }
        return new_node;
    }
};