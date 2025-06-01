class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        arr = []

        for x in range(1, n + 1):
            if x % 3 == 0:
                if x % 5 == 0:
                    arr.append("FizzBuzz")
                else:
                    arr.append("Fizz")
            elif x % 5 == 0:
                arr.append("Buzz")
            else:
                arr.append(str(x))
            
        
        return arr