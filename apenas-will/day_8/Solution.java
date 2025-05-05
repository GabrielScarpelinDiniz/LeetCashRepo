/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode();
        int rest = 0;
        ListNode c = head;
        ListNode c1 = l1;
        ListNode c2 = l2;

        while(c1 != null || c2 != null){
            int val1 = c1 == null? 0: c1.val;
            int val2 = c2 == null? 0: c2.val;

            if((val1 + val2 + rest) >= 10){
                c.val = (val1 + val2 + rest) % 10;
                rest = 1;
            } else {
                c.val = val1 + val2 + rest;
                rest = 0;
            }

            if(c1 != null) c1 = c1.next;
            if(c2 != null) c2 = c2.next;
            if (c1 != null || c2 != null){
                c.next = new ListNode();
                c = c.next;
            }
        }
        if(rest == 1){
            c.next = new ListNode(1);
        }
        
        return head;

    }
}