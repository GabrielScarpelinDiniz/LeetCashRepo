class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        menor = float('inf')
        segundo_menor = float('inf')

        for i in nums:
            if i <= menor:
                menor = i
            elif i <= segundo_menor:
                segundo_menor = i
            else:
                return True

        return False 
        
        
        return False

Vibe de poucas palavras. Tinha feito uma solucao O(n³), eu gostava muito dela mas nao rodou. Depois quase me matei caçando uma alternativa viavel. Achei essa: duas variaveis, menor e segundo menor. Se eu acho um menor que menor vira menor, se eu acho um que não é menor que menor mas é menor que o segundo menor vira segundo menor. Se eu acho um que nao é menor que o menor nem que o segundo menor entao ele so pode ser o terceiro maior. Consequentemente temos uma trinca.