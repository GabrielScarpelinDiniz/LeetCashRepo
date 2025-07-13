class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for i in hours:
            if i >= target:
                count += 1
        
        return count

Percorro a lista de horas com um contador, para cada funcionario que igualar ou superar a quantidade de hoaras espearada eu somo no contador e ao final eu retorno o contador. Trivial.