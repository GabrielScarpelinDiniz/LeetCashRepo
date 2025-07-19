class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        pointerG = 0
        pointerS = 0
        
        while pointerS < len(s) and pointerG < len(g):
            if s[pointerS] >= g[pointerG]:
                pointerG += 1
            pointerS += 1
        
        return pointerG