class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        dic = {}
        ans = []

        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                ans.append(i)
        
        return ans

        