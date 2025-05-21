class Solution(object):
    def intersection(self, nums1, nums2):
        lista3=[]
        dicionario = {}
        for i in range(len(nums1)):
            if dicionario.get(nums1[i]) != 0:
                dicionario[nums1[i]] = 1

        for i in range(len(nums2)):
            if dicionario.get(nums2[i]) == 1:
                dicionario[nums2[i]] += 1

        for n in dicionario:
            if dicionario[n] == 2:
                lista3.append(n)
        return lista3

solution = Solution
lista1 = [1,1,2,2,3,3,4,4]
lista2 = [1,2,3]
print(solution.intersection(None, lista1,lista2))

        