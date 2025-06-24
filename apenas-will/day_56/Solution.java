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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // Both null
        if(list1 == null && list2 == null) return null;

        // One of them null
        if(list1 == null) return list2;
        if(list2 == null) return list1;
        
        // None null
        ListNode current1 = list1;
        ListNode current2 = list2;
        ListNode res = new ListNode();
        ListNode current = res;

        while(current1 != null || current2 != null){
            if(current1 != null && current2 != null){
                if(current1.val <= current2.val){
                    current.next = current1;
                    current = current.next;
                    current1 = current1.next;
                } else {
                    current.next = current2;
                    current = current.next;
                    current2 = current2.next;
                }
            } else if (current1 != null){
                current.next = current1;
                current = current.next;
                current1 = current1.next;
            } else {
                current.next = current2;
                current = current.next;
                current2 = current2.next;
            }
        }

        return res.next;
    }
}