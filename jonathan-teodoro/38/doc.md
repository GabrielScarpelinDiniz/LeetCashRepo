```python
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        result = "1"
        for _ in range(2, n + 1):
            new_result = ""
            i = 0
            while i < len(result):
                count = 1
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    count += 1
                    i += 1
                new_result += str(count) + result[i]
                i += 1
            result = new_result

        return result
``` 
O código começa com o termo "1". Depois, repete um laço até chegar no n desejado. Em cada repetição, ele percorre o termo atual, conta quantos dígitos iguais estão em sequência e monta um novo termo com essa contagem seguida do dígito. No fim, retorna o termo gerado.
Por exemplo, "1" vira "11" (um 1), depois "21" (dois 1s), "1211" (um 2, um 1) e assim por diante, até chegar no n desejado.