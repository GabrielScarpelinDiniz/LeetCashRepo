Exercício bem tranquilinho hoje:

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = 0
        for num_of_candies in candies:
            if num_of_candies > max_candies:
                max_candies = num_of_candies
        
        print(max_candies)
        answer = []
        for i in candies:

            if i+extraCandies>=max_candies:
                answer.append(True)
            else:
                answer.append(False)

        print(answer)
        return answer
        

                    
Percorro a lista de doces e busco quem tem mais.
Depois percorro novamente somando os extra candies para cada um e comparando com o máximo.
Simples e fácil.

5/5 do Mr. Computareiro.
