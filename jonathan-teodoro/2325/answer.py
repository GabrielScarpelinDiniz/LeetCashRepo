class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        seen = set()
        substitution = {}
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        index = 0
        for char in key:
            if char.isalpha() and char not in seen:
                substitution[char] = alphabet[index]
                seen.add(char)
                index += 1
                if index == 26:
                    break

        decoded = []
        for char in message:
            if char == ' ':
                decoded.append(' ')
            else:
                decoded.append(substitution[char])
        
        return ''.join(decoded)