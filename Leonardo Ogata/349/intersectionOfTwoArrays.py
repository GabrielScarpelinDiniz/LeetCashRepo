class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            longer, shorter = nums1, nums2
        else:
            shorter, longer = nums1, nums2

        auxArr = []
        
        for i in range(len(shorter)):
            if shorter[i] in longer and shorter[i] not in auxArr:
                auxArr.append(shorter[i])

        return auxArr
            
