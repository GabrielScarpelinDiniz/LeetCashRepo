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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if(head.next == null){
            if(n == 1) return null;
            else return head;
        }
        int l = 0;
        ListNode prev = new ListNode();
        prev.next = head;
        ListNode current = head;
        ListNode next = head.next;

        for(int i = 1; i < n ; i++){
            next = next.next;
        }

        while(next != null){
            l++;
            prev = prev.next;
            current = current.next;
            next = next.next;
        }

        prev.next = current.next;
        current = null;

        if(l + n == n) return prev.next;

        return head;
    }
}