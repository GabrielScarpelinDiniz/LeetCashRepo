class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lista = nums1 + nums2
        lista.sort()
        n = len(lista)
        
        if n % 2 != 0:
            mid_index = n // 2
            return float(lista[mid_index])
        else:
            mid1 = n // 2
            mid2 = mid1 - 1
            return (lista[mid1] + lista[mid2]) / 2.0
