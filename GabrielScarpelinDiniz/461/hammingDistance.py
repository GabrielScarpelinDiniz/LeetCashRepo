class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_bin = bin(x).split("b")[1]
        y_bin = bin(y).split("b")[1]

        len_x_bin = len(x_bin)
        len_y_bin = len(y_bin)

        print(x_bin)
        print(y_bin)

        if len_x_bin < len_y_bin:
            x_bin = ("0" * (len_y_bin - len_x_bin)) + x_bin

        elif len_x_bin > len_y_bin:
            y_bin = ("0" * (len_x_bin - len_y_bin)) + y_bin

        max_len = max(len_x_bin, len_y_bin)
        print(x_bin)
        print(y_bin)
        idx = 0
        result = 0
        while idx < max_len:
            print(x_bin[idx])
            print(y_bin[idx])
            if x_bin[idx] != y_bin[idx]:
                result += 1
            idx += 1

        return result
