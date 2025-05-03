class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        chars = digits.split("")
        map_digits = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w", "x","y","z"]
        }
        combinations = []
        digits_len = len(chars)

        if digits_len > 0:
            for i in range(0, len(map_digits[chars[0]])):
                if digits_len > 1:
                    for j in range(0, len(map_digits[chars[1]])):
                        if digits_len > 2:
                            for k in range(0, len(map_digits[chars[2]])):
                                if digits_len > 3:
                                    for l in range(0, len(map_digits[chars[3]])):
                                        combinations.append(map_digits[chars[0]][i] + map_digits[chars[1]][j] + map_digits[chars[2]][k] + map_digits[chars[3]][l])
                                else:
                                    combinations.append(map_digits[chars[0]][i] + map_digits[chars[1]][j] + map_digits[chars[2]][k])
                        else:
                            combinations.append(map_digits[chars[0]][i] + map_digits[chars[1]][j])
                else:
                    combinations.append(map_digits[chars[0]][i])

        return combinations
