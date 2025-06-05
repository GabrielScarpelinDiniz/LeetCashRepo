class Solution(object):
    def isHappy(self, n):
        try:
            lista = set()
            while n!=1:
                somatorio = 0
                while n>0:
                    somatorio+=((n%10)**2)
                    n//=10
                if somatorio in lista:
                    return False
                lista.add(somatorio)
                n=somatorio
            return True
        except Exception as e:
            return False