# Problem 412

> Given an integer n, return a string array answer (1-indexed) where:

> answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
> answer[i] == "Fizz" if i is divisible by 3.
> answer[i] == "Buzz" if i is divisible by 5.
> answer[i] == i (as a string) if none of the above conditions are true.

# How the problem works?

It's a very simple problem that we only need to verify if the number is divisible by 3 or 5 (or 3 and 5) and append something on the final based on the (index + 1)

# How I solve the problem?

I just create an array and a iterator variable. If some condition are accepted, I add on the final the thing needed. Otherwise, I just add the number at the final on the array.
