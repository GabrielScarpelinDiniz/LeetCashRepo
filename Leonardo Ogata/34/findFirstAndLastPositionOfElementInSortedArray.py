class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums)
        arr = []

        if not nums:
            return [-1, -1]

        while low <= high:
            
            mid = low + (high - low) // 2

            if mid >= len(nums):
                break

            print(mid)

            if nums[mid] == target:
                for i in range(mid -1, -1, -1):
                    if nums[i] == target:
                        arr.append(i)
                    else:
                        break

                for i in range(mid, len(nums)):
                    if nums[i] == target:
                        arr.append(i)
                    else:
                        break

                if len(arr) == 1:
                    print(arr)
                    return [arr[0], arr[0]]
                else:
                    print(arr)
                    return(min(arr), max(arr))
                
            elif nums[mid] < target:
                low = mid + 1
            
            elif nums[mid] > target:
                high = mid - 1

        if len(arr) == 0:
            return [-1, -1]     