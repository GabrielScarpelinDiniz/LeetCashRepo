class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        dic = {}

        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        arr = []

        for i in dic:
            arr.append(i)

        arr.sort(reverse=True)

        if len(dic) == 3:
            return arr[-1] 
        elif len(dic) > 3:
            return arr[2]
        else:
            return max(arr)

        
        