class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        freq = 0
        val = 0
        arr = []

        for i in range (0, len(nums), 2):
            freq = nums[i]
            val = nums[i+1]
            arr += [val] * freq
    
        return arr