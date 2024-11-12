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
    ListNode* reverseKGroup(ListNode* head, int k) {
        auto ptr = head;
        int n = 0;
        while (ptr) {
            n += 1;
            ptr = ptr->next;
        }
        if (n < k) {
            return head;
        }
        auto dum = split(head, k);
        auto a = reverseKGroup(dum, k);
        auto c = reverselist(head, k);
        head->next=a;
        
        return c;
    }

private:
    ListNode* split(ListNode* head, int k) {
        while (k > 1) {
            head = head->next;
            k--;
        }
        auto fur = head->next;
        head->next = nullptr;
        return fur;
    }

    ListNode* reverselist(ListNode* head, int k) {
        ListNode* prev = nullptr;
        ListNode* curr = head;
        while (k > 0 && curr) {
            ListNode* nextTemp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nextTemp;
            k--;
        }
        return prev;
    }
};
