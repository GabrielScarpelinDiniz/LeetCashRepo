class Solution:
    def getSneakyNumbers(self, nums):
        freq = {}      
        result = []    
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for num in freq:
            if freq[num] == 2:
                result.append(num)

        return result
