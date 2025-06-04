``` python
class Solution(object):
    def romanToInt(self, s):
        romanos = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        ultimo = 0

        for i in reversed(s):
            valor = romanos[i]
            if valor < ultimo:
                total -= valor  
            else:
                total += valor 
            ultimo = valor

        return total
``` 
            
Cara eu confesso que falhei, tentei fazer com hashmap mas não mandei bem. Em minha defesa, to cansado, joguei bola pra caceta, e apaguei, tive que acordar só pra fazer essa bomba,logo relevem pf. Em algum momento eu resolvo com hashmap. hoje eu fiz um dict basico, com cada e depois pra cda item de tras prea frente fui pegando o respectivo valor. Deu bom assim! Ideal? Não. Funcional? Sim