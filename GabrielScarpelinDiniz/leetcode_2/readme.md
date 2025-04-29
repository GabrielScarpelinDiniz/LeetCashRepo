# Problem 2 - Add two numbers

> You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

> You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## How the problem works?

So, we it's simple, but the rust make the things more complicated... We need only sum the equivalent numbers in the linked list. And check if the number needs a carry. How my logic works?

1. Initiate the first element of the result linked list with the module of the sum of the first element of each linked list. Like: first_element(head) = (first_element_list1 + first_element_list2) % 10. Why the module? Because in the decimal numbers, we cannot have any numbers biggest than 9 in a column
2. If the result is biggest than 9, we need to add a carry = 1 for the next number.
3. Adds the result on the final of the linked list.
4. Run the steps 2 and 3 and 4 inside a loop, verifying if the element of the first linked list or the second linked list is empty. Because if one of these are emptys we need only to look to one value.


## Rust advantages
I don't recommend use rust on technical problems. It's so complex to do something simple like the code of this exercise. For sure, if I made this in python, I probably take around 2x less time. But, if you are interested in a language complex like rust, feel free to try. With rust I beat 98% of solutions in usage memory and get a runtime of 0ms. Thats sounds great!
