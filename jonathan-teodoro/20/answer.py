class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapa = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapa.values():
                stack.append(char)
            elif char in mapa:
                if not stack or stack[-1] != mapa[char]:
                    return False
                stack.pop()
            else:
                return False
        
        return not stack
