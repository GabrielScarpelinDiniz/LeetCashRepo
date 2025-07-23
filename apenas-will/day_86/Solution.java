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
    public boolean isPalindrome(ListNode head) {
        ListNode current = head;
        List<ListNode> nodes = new ArrayList<>();

        while(current != null){
            nodes.add(current);
            current = current.next;
        }

        int a = 0, b = nodes.size() - 1;

        while(a < b){
            if(nodes.get(a).val != nodes.get(b).val) {
                return false;
            }
            a ++;
            b --;
        }

        return true;
    }
}