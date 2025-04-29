use std::boxed::Box;
use std::option::Option;
// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}
pub fn add_two_numbers(
    l1: Option<Box<ListNode>>,
    l2: Option<Box<ListNode>>,
) -> Option<Box<ListNode>> {
    let mut element1 = l1.unwrap();
    let mut element2 = l2.unwrap();

    let mut sum = element1.val + element2.val;
    let mut carry = 0;
    let mut head = Box::new(ListNode::new(sum % 10));
    let mut current = &mut head;
    if sum > 9 {
        carry = 1;
    }

    while element1.next.is_some() || element2.next.is_some() {
        if element1.next.is_some() && element2.next.is_none() {
            element1 = element1.next.unwrap();
            sum = element1.val + carry;
            carry = 0;
            if sum > 9 {
                carry = 1;
            }
            continue;
        } else if element2.next.is_some() && element1.next.is_none() {
            element2 = element2.next.unwrap();
            sum = element2.val + carry;
            carry = 0;
            if sum > 9 {
                carry = 1;
            }
            current.next = Some(Box::new(ListNode::new(sum % 10)));
            current = current.next.as_mut().unwrap();
            continue;
        }
        element1 = element1.next.unwrap();
        element2 = element2.next.unwrap();
        sum = element1.val + element2.val + carry;
        carry = 0;
        if sum > 9 {
            carry = 1;
        }
        current.next = Some(Box::new(ListNode::new(sum % 10)));
        current = current.next.as_mut().unwrap();
    }

    if carry > 0 {
        current.next = Some(Box::new(ListNode::new(1)));
    }

    Some(head)
}

fn main() {
    println!("Hello World!");
}
