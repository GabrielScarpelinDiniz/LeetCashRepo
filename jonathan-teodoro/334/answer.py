class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        menor = float('inf')
        segundo_menor = float('inf')

        for i in nums:
            if i <= menor:
                menor = i
            elif i <= segundo_menor:
                segundo_menor = i
            else:
                return True

        return False 
        
        
        return False