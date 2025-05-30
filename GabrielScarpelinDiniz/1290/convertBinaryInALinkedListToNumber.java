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

    public int getDecimalValue(ListNode head) {
        ArrayList<Boolean> bits = new ArrayList();
        ListNode current = head;
        while (current != null) {
            if (current.val == 0) {
                bits.add(false);
            } else {
                bits.add(true);
            }
            current = current.next;
        }

        int idx = bits.size() - 1;
        int base = 0;
        int result = 0;
        while (idx >= 0) {
            if (bits.get(idx)) {
                result += Math.pow(2, base);
            }
            base++;
            idx--;
        }
        return result;
    }
}
