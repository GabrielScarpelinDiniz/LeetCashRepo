class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_value = 0
        for i in accounts:
            sum = 0
            for j in i:
                sum += j
            
            max_value = max(max_value, sum)
        
        return max_value

percorro como se fosse uma matriz, gero uma variavel sum que para cada item do array principal é incrementada com cada item percorrido no dentro desse array, ao final de cada item do array principal, comparo seu valor com o maior ate agora, se for maior eu substituo, se não eu troco.