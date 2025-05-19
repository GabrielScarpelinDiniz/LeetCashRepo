class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary_control, bits = bin(n).split("b")
        one_bits = 0
        for bit in bits:
            if bit == '1':
                one_bits += 1

        return one_bits
