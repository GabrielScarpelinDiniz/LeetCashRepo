class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {
            'a': 0,
            'e': 0,
            'i': 0,
            'o': 0,
            'u': 0
        }

        consonants = {
            'b': 0,
            'c': 0,
            'd': 0,
            'f': 0,
            'g': 0,
            'h': 0,
            'j': 0,
            'k': 0,
            'l': 0,
            'm': 0,
            'n': 0,
            'p': 0,
            'q': 0,
            'r': 0,
            's': 0,
            't': 0,
            'v': 0,
            'w': 0,
            'x': 0,
            'y': 0,
            'z': 0
        }

        for i in s:
            if i in vowels:
                vowels[i] += 1
            else: 
                consonants[i] += 1
        
        return max(vowels.values()) + max(consonants.values())
        