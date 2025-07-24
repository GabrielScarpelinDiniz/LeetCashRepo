class Solution:
    def decode(self, encoded, first):
        arr = [first]
        for e in encoded:
            arr.append(arr[-1] ^ e)
        return arr

O algoritmo aproveita a propriedade do XOR: se encoded[i] = arr[i] XOR arr[i + 1], então podemos recuperar arr[i + 1] fazendo arr[i] XOR encoded[i]. Começamos com arr[0] = first, e iteramos por encoded, decodificando cada próximo valor e adicionando à lista arr. No final, arr é exatamente a array original reconstruída