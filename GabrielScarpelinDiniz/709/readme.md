# Problem 709

> Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

# How does I solve the problem?

To solve the problem, I create a hashmap with all letters mapped to lower case, then I iterate by the array and save the final result (upper case to lower case) inplace at the array. Then I join the string in a array again and return the result.
