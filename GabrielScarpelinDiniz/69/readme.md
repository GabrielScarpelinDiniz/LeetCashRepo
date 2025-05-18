> Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

> You must not use any built-in exponent function or operator.

> For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# How does the problem works?

Given a number x, we need to return the approximate (or if has exactly sqrt, the exactly) square root of this number.

# How did I solve the problem?

To solve the problem I implement a initial number (0), and I increment this number while the number multiplied by theirself is lowest than the target value. Finally I made a check, because like 8 that we dont have exactly square root, I returned the previous floor rounded value.
