# Problem 141

> Given head, the head of a linked list, determine if the linked list has a cycle in it.

> There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

> Return true if there is a cycle in the linked list. Otherwise, return false.

# How does the problem work?

We need to check if the current element has appeared at the linked list before. If the element has appeared means that the linked list has a cycle (appoint to another element appeared before the current element)

# How did I solve the problem?

First, I initiate iterating by the Linked list with the followed strategy: Until the current element is not None, do something and current element receive the next element. And to check if has a cycle, I use a hashmap saving the reference, if the next of the current element has saved reference, its means that we have a cycle. If not, I save the current reference to the current node in the hashmap (the dictionary in python, which is very similar to a hashmap).
