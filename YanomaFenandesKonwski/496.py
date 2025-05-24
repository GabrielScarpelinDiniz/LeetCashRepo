class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        resultado = []
        for num in nums1:
            encontrou=False
            for i in range(len(nums2)):
                if num==nums2[i]:
                    encontrou=True
                    break
            if encontrou:
                resposta = -1
                for j in range(i+1, len(nums2)):
                    if num<nums2[j]:
                        resposta = nums2[j]
                        break
                resultado.append(resposta)
        return resultado