class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        has = {}
        ans = []

        for i in nums:
            if i not in has:
                has[i] = 1
            else:
                has[i] += 1
        

        for i in range(1, len(nums) + 1):
            if i not in has:
                ans.append(i)

        return ans

            


        