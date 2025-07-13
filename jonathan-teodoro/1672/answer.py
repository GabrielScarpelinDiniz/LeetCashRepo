class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_value = 0
        for i in accounts:
            sum = 0
            for j in i:
                sum += j
            
            max_value = max(max_value, sum)
        
        return max_value
