# Problem 1290

> Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

> Return the decimal value of the number in the linked list.

> The most significant bit is at the head of the linked list.

# How does I solve the problem?

To solve the problem, I start transforming the linked list in a array list (its more easier to manipulate). Then I applied a simple number convertion, if the number is 1 we take 2 raise in a power of the count of the current element starting at the final and sum in a variable. I sum all of this operations adding in a result variable until I finish the number.
