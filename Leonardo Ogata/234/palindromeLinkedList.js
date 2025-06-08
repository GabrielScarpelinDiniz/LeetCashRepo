/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    var current = head;
    const arr = [];


    while(current != null){
        arr.push(current.val);
        current = current.next;
    }

    const reverseArr = [...arr].reverse();

    return arr.every((val, i) => val === reverseArr[i]);
};