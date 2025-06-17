class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtracking(i, curStr):
            if len(curStr) == len(digits):
                result.append(curStr)
                return      
            
            for char in phone_map[digits[i]]:
                backtracking(i + 1, curStr + char) 
        
        if digits:
            backtracking(0, "")

        return result