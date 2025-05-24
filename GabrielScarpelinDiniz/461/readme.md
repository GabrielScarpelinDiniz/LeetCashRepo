# Problem 461

> The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

> Given two integers x and y, return the Hamming distance between them.

# How did the problem works?

We need to compare different bits looking to two numbers, and return the length of different bits

# How does I solve the problem?

First, I convert the two numbers in binary, then I add a pad in the two numbers. So, if the first number has lower quantity of bits compared with the second number, we add left zeros at the number (is the same number, we are not changing the number). Otherwise, if the second number has lower quantity, we add left zeros at the second number. Then, we can compare bit by bit to find the final result.
