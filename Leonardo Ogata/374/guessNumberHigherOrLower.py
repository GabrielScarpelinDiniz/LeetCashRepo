# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        high = n
        low = 0
        x = 0

        
        while True:

            mid = (low + high)//2
            print(mid)

            x = guess(mid)

            if x == 0:
                return mid
            
            elif x == -1:
                high = mid - 1
            
            elif x == 1:
                low = mid + 1




        