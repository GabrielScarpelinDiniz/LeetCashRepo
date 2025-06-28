# 61º Dia de LeetCash

Hoje eu resolvi o problema 1720 - Decode XORed Array, no qual dado um array `encoded`, onde `encoded[i] = arr[i] ^ arr[i+1]`, e o primeiro valor de `arr` (`first`), o objetivo é reconstruir o array original. Para isso eu segui os seguintes passos:

1. Começo com `arr = [first]`
2. Para cada `i` em `encoded`, aplico: `arr[i+1] = encoded[i] ^ arr[i]`
3. Retorno o array `arr` completo

E pronto, mais um exercício resolvido!!!