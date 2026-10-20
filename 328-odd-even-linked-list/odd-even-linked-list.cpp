class Solution {
 public:
  ListNode* oddEvenList(ListNode* head) {
    ListNode oddHead(0);
    ListNode evenHead(0);
    ListNode* odd = &oddHead;
    ListNode* even = &evenHead;

 
