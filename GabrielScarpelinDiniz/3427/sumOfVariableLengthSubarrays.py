class Solution:
    def subarraySum(self, nums) -> int:
        subarrays_sum = 0
        for i in range(len(nums)):
            start = max(0, i - nums[i])
            subarrays = nums[start:i + 1]
            sum_sub = 0
            for num in subarrays:
                sum_sub += num

            subarrays_sum += sum_sub

        return subarrays_sum
