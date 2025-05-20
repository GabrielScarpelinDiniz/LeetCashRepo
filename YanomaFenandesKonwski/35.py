class Solution(object):
    def searchInsert(self, nums, target):
        
        direita=0
        esquerda = len(nums)-1

        while(direita<=esquerda):
            meio = (direita+esquerda)//2
            if (nums[meio] == target):
                return meio
            else:
                if (nums[meio]<target):
                    direita = meio+1
                else:
                    esquerda = meio-1
            
        return direita


        