class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        not_appear = None
        set_items = set()
        potential_items = set()
        for i in nums:
            if i not in set_items:
                potential_items.add(i)
                set_items.add(i)
            else:
                if i in potential_items:
                    potential_items.remove(i)
        for x in potential_items:
            return x
