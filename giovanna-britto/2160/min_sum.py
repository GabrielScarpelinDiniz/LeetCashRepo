class Solution:
    def minimumSum(self, num: int) -> int:
        string = str(num)
        arr = list(string)
        arr.sort()
        num1 = arr[0] + arr[2]
        num2 = arr[1] + arr[3]

        return int(num1) + int(num2)