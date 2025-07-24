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
    public ListNode swapNodes(ListNode head, int k) {
        ListNode prev1 = new ListNode(), prev2 = new ListNode(), swap1 = head, swap2 = head;
        prev1.next = head;
        prev2.next = head;

        for(int i = 1; i < k; i++){
            prev1 = prev1.next;
            swap1 = swap1.next;
        }

        ListNode end = swap1.next;
        int i = 0;
        while(end != null){
            swap2 = swap2.next;
            prev2 = prev2.next;
            end = end.next;
            i++;
        }
        i += k;

        prev1.next = swap2;
        prev2.next = swap1;

        ListNode temp = swap1.next;

        swap1.next = swap2.next;
        swap2.next = temp;

        if(k == 1) return swap2;
        if(k == i) return swap1;

        return head;
    }
}