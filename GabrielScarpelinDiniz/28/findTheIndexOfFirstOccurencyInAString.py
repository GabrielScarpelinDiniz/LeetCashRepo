class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        fst_occurs_idx = -1
        substr = ""
        sub_idx = 0
        idx = 0
        if len(needle) > len(haystack):
            return -1
        while idx < len(haystack):
            i = haystack[idx]
            if i == needle[sub_idx]:
                if fst_occurs_idx == -1:
                    fst_occurs_idx = idx
                substr += i
                sub_idx += 1
            else:
                if fst_occurs_idx != -1:
                    idx = fst_occurs_idx
                fst_occurs_idx = -1
                substr = ""
                sub_idx = 0

            if needle == substr:
                return fst_occurs_idx
            idx += 1
        print(substr)
        if needle != substr:
            return -1
        return fst_occurs_idx
