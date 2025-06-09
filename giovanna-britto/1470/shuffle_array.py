class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arrX = []
        arrY = []
        arrF = []

        for i in range(len(nums)):
            if (i < n):
                arrX.append(nums[i])
            else:
                arrY.append(nums[i])

        for i in range(n):
            arrF.append(arrX[i])
            arrF.append(arrY[i])
    
        
        return arrF

