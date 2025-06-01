Pegamos os números digitados (de 2 a 9) e transforma cada um nas letras que ele representa no teclado do celular. A ideia é começar com as letras do primeiro número e ir juntando com as letras do próximo, formando todas as combinações possíveis. Por exemplo, se o número for "23", ele começa com as letras do 2 (a, b, c) e vai combinando com as letras do 3 (d, e, f), formando pares como ad, ae, af, bd e assim por diante, até ter todas as misturas possíveis.

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

            