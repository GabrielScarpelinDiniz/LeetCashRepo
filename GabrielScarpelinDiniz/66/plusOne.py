class Solution(object):
    def plusOne(self, digits):
        current = len(digits) - 1
        digits[current] = digits[current] + 1
        while digits[current] > 9:
            digits[current] = 0
            if current - 1 >= 0:
                digits[current - 1] = digits[current - 1] + 1
                current = current - 1
            else:
                digits.insert(0, 1)

        return digits
