# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        l = 1
        r = n
        choice = int((l+r)/2)

        while l<=r:
            print(choice)
            result = guess(choice)
            print(result)
            print('---')

            if result == 0:
                return choice

            elif result == 1:
                l = choice + 1
                choice = int((l+r)/2)
            
            elif result == -1:
                r = choice - 1 
                choice = int((l+r)/2)

        return 'nao'

Exercicio trival de Binary Search!!!!
Demorei pra entender o enunciado mas apenas isso. 
Binary search implementada de forma interativa bem delicinha. Se é maio muda o l e consequentement o choice, se  é menor o r e o choice. GO NEXT!

