class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        primeiro = start
        for i in range(1, n):
            primeiro ^= start + 2 * i
        return primeiro