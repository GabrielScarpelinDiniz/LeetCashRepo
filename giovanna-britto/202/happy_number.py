class Solution:
    def get_next(self, number):
        return sum(int(num)** 2 for num in str(number))
        
    def isHappy(self, n: int) -> bool:
        aux = set()

        while n != 1 and n not in aux:
            aux.add(n)
            n = self.get_next(n)
        return n == 1

       