class Solution:
    def singleNumber(self, nums) -> int:
        val = 0
        for i in nums:
            val = val ^ i
        return val;

if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([4, 1, 2, 1, 2]))
    print(s.singleNumber([2, 2, 1]))
    print(s.singleNumber([1]))
    print(s.singleNumber([1, 0, 0]))
    print(s.singleNumber([0, 0, 0, 1]))
    print(bin(3))
    print(bin(5))
    print(int(0b110))