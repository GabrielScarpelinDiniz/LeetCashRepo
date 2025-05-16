class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:


        def binary_search(nums,target):
            l = 0
            r = len(nums)-1
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                    
                elif nums[mid]>target:
                    r = mid - 1
                    
                elif nums[mid] < target:
                    l = mid+1
            
            return -1
        
        result = binary_search(nums, target)
        print(result)
        if result == -1:
            nums.append(target)
            nums.sort()
            result = binary_search(nums, target)
        return result


        

Binary search classica, iterativa (recursiva é viadagem)
Defino dois ponteiros, L e R. E pego o MID entre eles. E comparo o valor desse indice no array. Se for igual ao target retorno resultado, se nao eu vou mudando o L e R. Feita binary search. Confiro o return, se for -1 eu rodo novamente com o valor a mais.