class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicS = Counter(s)
        dicT = Counter(t)

        return dicS == dicT