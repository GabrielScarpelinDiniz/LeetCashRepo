class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def combinar(letras_atuais, proxima_letra):
            nova_lista = []
            for prefixo in letras_atuais:
                for letra in proxima_letra:
                    nova_lista.append(prefixo + letra)
            return nova_lista

        resultado = list(phone_map[digits[0]])

        for d in digits[1:]:
            letras = phone_map[d]
            resultado = combinar(resultado, letras)

        return resultado

            