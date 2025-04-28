class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict_1 = set()
        answer = []
        for item in nums1:
            if item not in dict_1:
                dict_1.add(item)
            
        
        for value in nums2:
            if value in dict_1 and value not in answer:
                answer.append(value)

        return answer
        