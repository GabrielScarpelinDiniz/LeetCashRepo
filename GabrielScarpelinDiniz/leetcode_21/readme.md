# Problem 21

> You are given the heads of two sorted linked lists list1 and list2.
> Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

> Return the head of the merged linked list.

## How the problem works?

We need to look to each sorted array, and merge the both, mantaining the final array sorted.

## How I solve the Problem

First, I create two references, the l1 pointer, that saves the references for the first array/list element that we are accessing and the l2 pointer, that does the same. First, we compare the element from the first array with the element with the second array. If the element from the first array is more biggest than the element from the second array, we put the element from the second array in our final array, and move the pointer from the second array to the next element. If the element from the first array is more lowest, we do the same with the element from the first array.

So, we repeat these steps until all elements from both arrays are visited.
