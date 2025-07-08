class Solution:
    def countSegments(self, s: str) -> int:
        if not s:
            return 0
            
        arr = []
        aux = []

        for i in range(len(s)):
            if s[i] != " ":
                aux.append(s[i])
            elif s[i] == " " and aux:
                arr.append(aux)
                aux = []
        if aux:
            arr.append(aux)
        
        return len(arr)