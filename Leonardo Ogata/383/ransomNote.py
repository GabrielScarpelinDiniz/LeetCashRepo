class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arrM = []

        for i in magazine:
            arrM.append(i)

        for j in ransomNote:
            if j in arrM:
                arrM.pop(arrM.index(j))
            else:
                return False
        
        return True
        