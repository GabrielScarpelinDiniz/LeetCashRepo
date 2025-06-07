class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sum = 0
        for i in range(1,n+1):
            if i%3 == 0 or i%5 == 0 or i%7 ==0:
                print(i)
                sum += i
        
        return sum

    
MUITO FACIL, MUITO MESMO! O MAIS FACIL ATE AGORA!
Percorro se ao dividir por 3 5 ou 7 der resto 0, estouramos e somamos. Aulas dms! 