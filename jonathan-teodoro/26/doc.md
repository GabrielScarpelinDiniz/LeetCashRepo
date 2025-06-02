class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
        for i in nums:
            if i not in arr:
                arr.append(i)
        
        for i in range(len(arr)):
            nums[i] = arr[i]
        
        return len(arr)
        

Não me orgulho muito dessa resolução. Acho que falhei na lógica algoritmica. Claramente existem melhores formas de se resolver esse exercício, inclusive sendo O(n). Busquei essa alternativa mas falhei miseravelmente. Não encontrei. Se em outro momento eu decidir enfrentar esse desafio novamente, trarei atualizações, mas, por enquanto, não cheguei lá. A partir disso, posso explicar o que foi feito. Percorro a lista e encontro todos os valores unicos, adicionando-os em um array auxiliar. Apos isso, percorro esse array auxiliar preenchedo no principal os valores encontrados. Assim é bem trivial resolvê-lo, mas sei que poderia ir além. Beijo do computareiro até a proxima.