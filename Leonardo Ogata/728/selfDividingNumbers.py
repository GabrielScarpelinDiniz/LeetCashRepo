class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        arr = []

        for i in range(left, right + 1):
            div = True
            auxI = i
            resto = 0
            while auxI > 0:
                resto = auxI % 10
                auxI =  auxI//10
                if resto == 0 or i % resto != 0:
                    div = False
            
            if div:
                arr.append(i)

        return arr
            

                
        