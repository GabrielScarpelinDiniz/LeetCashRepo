``` python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s = "".join(sorted(s))
        t = "".join(sorted(t))

        for i in range(len(s)):
            if s[i] == t[i]:
                continue
            return False
        
        return True
    
``` 

Nessa eu aprendi uma paradinha util, que não havia pensado. Como ordenar uma string em python. Claro, há formas mais manuais de se fazer - converter em uma lista e depois concatenar item a item. Mas eu quero simplificidade para ganhar tempo em possiveis entrevistas. Aprendi o metodo ```s = "".join(sorted(s))``` que funciona muito bem. Feito isso, eu vou item a item comparando se eles batem, se sim, exercicio concluido. (Existem formas mais simples mas isso foi o que pensei inicialmente)