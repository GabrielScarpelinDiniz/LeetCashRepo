class Solution(object):
    def subtractProductAndSum(self, n):
        multiplica = 1
        soma = 0
        numero = 0
        while n>0:
            numero = n%10
            print(numero)
            n //= 10
            soma += numero
            multiplica=multiplica*numero
            print(soma)
            print(multiplica)
        return (multiplica - soma)

        