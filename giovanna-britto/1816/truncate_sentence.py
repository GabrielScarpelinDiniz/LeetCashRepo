class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        newS = s.split(' ')
        newS = newS[0:k]

        return ' '.join(newS)