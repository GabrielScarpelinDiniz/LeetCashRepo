class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        big = 0
        aux = 0

        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                aux += accounts[i][j]
                
            if aux > big:
                big = aux
            aux = 0
        
        return big
                
        