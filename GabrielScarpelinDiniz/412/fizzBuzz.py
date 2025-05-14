class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        idx = 0
        arr = []
        while idx < n:
            if (idx + 1) % 3 == 0 and (idx + 1) % 5 == 0:
                arr.append("FizzBuzz")
            elif (idx + 1) % 3 == 0:
                arr.append("Fizz")
            elif (idx + 1) % 5 == 0:
                arr.append("Buzz")
            else:
                arr.append(str(idx + 1))

            idx += 1

        return arr
