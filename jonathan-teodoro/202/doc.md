class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        
        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            sum = 0

            for i in str(n):
                square = int(i)*int(i)
                sum += square
            n = sum
        
        return True


Exercicio da avaliação diagnóstica para evitar problemas posteriores. Confesso que demorei pra entender o enunciado, não tinha ficadod claro quando eu identificaria o fim do ciclo. Entendo isso facilitou! While que espera n ser igual a um, se não rodamos um for que substitui o n pelo quadrado de seus digitos, feito isso conferimos se esse valor ja foi visto. Se sim, marcha, se não, dentro! 