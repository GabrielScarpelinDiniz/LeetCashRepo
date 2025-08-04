class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
                return 1

        def fibonacci(n: int):
            if n == 0:
                return 0

            elif n == 1 or n == 2:
                return 1

            else:
                return fibonacci(n-1) + fibonacci(n-2)

        summer = 0

        summer = fibonacci(n - 1) + fibonacci(n - 2)
        
        return summer

        

        