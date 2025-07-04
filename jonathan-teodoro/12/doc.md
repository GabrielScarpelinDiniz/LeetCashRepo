Criando uma lista de tuplas, com os simbolos pareados com seus respectivos números (tipo 1000 com "M", 900 com "CM" e por aí vai) em ordem decrescente. Depois, ele percorre essa lista e, pra cada par, vai tirando aquele valor do número original o máximo de vezes possível, enquanto soma o símbolo correspondente numa string. No fim das contas, ele vai construindo o número romano pedaço por pedaço, do maior pro menor, até o número virar zero.

class Solution:
    def intToRoman(self, num):
        val_romans = [
            (1000, "M"),
            (900,  "CM"),
            (500,  "D"),
            (400,  "CD"),
            (100,  "C"),
            (90,   "XC"),
            (50,   "L"),
            (40,   "XL"),
            (10,   "X"),
            (9,    "IX"),
            (5,    "V"),
            (4,    "IV"),
            (1,    "I")
        ]
        
        roman = ""
        for val, symbol in val_romans:
            while num >= val:
                roman += symbol
                num -= val
        
        return roman
