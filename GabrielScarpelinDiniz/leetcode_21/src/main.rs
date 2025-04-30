use std::thread::current;

fn main() {
    println!("Hello, world!");
}

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

pub fn merge_two_lists(
    list1: Option<Box<ListNode>>,
    list2: Option<Box<ListNode>>,
) -> Option<Box<ListNode>> {
    if list1.is_none() {
        return list2;
    } else if list2.is_none() {
        return list1;
    } else if list1.is_none() && list2.is_none() {
        return list1;
    }
    let mut l1_current = list1;
    let mut l2_current = list2;

    let mut head = Box::new(ListNode::new(0));

    let mut current = &mut head;

    while l1_current.clone().is_some() || l2_current.clone().is_some() {
        if l1_current.clone().is_some() && l2_current.clone().is_some() {
            if l1_current.clone().unwrap().val > l2_current.clone().unwrap().val {
                current.next = Some(Box::new(ListNode::new(l2_current.clone().unwrap().val)));
                l2_current = l2_current.unwrap().next;
            } else {
                current.next = Some(Box::new(ListNode::new(l1_current.clone().unwrap().val)));
                l1_current = l1_current.unwrap().next;
            }
            current = current.next.as_mut().unwrap();
        } else {
            if l2_current.clone().is_some() {
                current.next = Some(Box::new(ListNode::new(l2_current.clone().unwrap().val)));
                current = current.next.as_mut().unwrap();
                l2_current = l2_current.unwrap().next;
            } else {
                current.next = Some(Box::new(ListNode::new(l1_current.clone().unwrap().val)));
                current = current.next.as_mut().unwrap();
                l1_current = l1_current.unwrap().next;
            }
        }
    }

    head.next
}
