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
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null) return null;
        ListNode sl = head;
        ListNode fa = head;

        while(fa != null){
            if(sl.val == fa.val){
                fa = fa.next;
            } else {
                sl.next = fa;
                sl = sl.next;
                fa = fa.next;
            }
        }
        sl.next = fa;

        return head;
    }
}