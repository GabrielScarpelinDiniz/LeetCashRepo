class Solution:
    def reverseDegree(self, s: str) -> int:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        total = 0
        for i in range(len(s)):
            reverse_value = 26 - alphabet.index(s[i])
            total += reverse_value * (i + 1)
        return total