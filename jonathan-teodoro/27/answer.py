class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        resp = nums.copy()
        nums.clear()
        print(resp)
        for idx, value in enumerate(resp):
            if value != val:
                nums.append(value)
        
        return len(nums)
        