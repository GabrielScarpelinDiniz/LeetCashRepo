class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        cont = 0
        indice = 0

        if (ruleKey == "type"):
            indice = 0
        elif (ruleKey == "color"):
            indice = 1
        else:
            indice = 2

        for item in items:
            if (item[indice] == ruleValue):
                cont += 1
        
        return cont
        