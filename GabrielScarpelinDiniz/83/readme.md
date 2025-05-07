# Problem 83

> Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# How the problem works?

We need to remove all duplicates element from linked lists, and to remove we need to consider that the next element will be linked with the last element (the element that appears before the duplicated)

# How I solve the problem?

I start using a hashmap to verify if the value has appeared. If the value has appeared, we need to link the next element with the last element, this will remove the current elemenent from the array. After this, we move our pointer (current) to the next, but not move the pointer that saves the last element. Otherwise, if the element has not appeared, we only move the current pointer to the next, and last pointer to current.
