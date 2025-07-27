class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        aux1 = []
        aux2 = []
        ans = []

        for i in range(n):
            aux1.append(nums[i])
        
        for i in range(n, len(nums)):
            aux2.append(nums[i])

        for i in range(len(aux1)):
            ans.append(aux1[i])
            ans.append(aux2[i])

        return ans