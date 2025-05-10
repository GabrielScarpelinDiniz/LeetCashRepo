# Problem 28

> Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# How the problem works?

We need to return the first occurence of a substring in a major string.

# How I solve the problem?

To solve the problem I start searching for the same initial letter in the string. If those letters match, we move an pointer to the next letter of the needle. Although, if the first occurrence can be a part of the next string, we move the pointer to the next letter (Not to the final of the possible occurence, because some letter of this partial match can be a letter of the correct needle.)
