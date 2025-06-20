## Maior Palíndromo (Longest Palindrome)

O método `LongestPalindrome` retorna o comprimento do maior palíndromo que pode ser construído com as letras de uma string.

**Funcionamento:**
1. Conta a frequência de cada caractere.
2. Soma todos os pares de caracteres (cada par pode ser usado simetricamente no palíndromo).
3. Se houver pelo menos um caractere com frequência ímpar, adiciona 1 ao resultado (esse caractere pode ficar no centro do palíndromo).

**Exemplos:**
- Entrada: "abccccdd" → Saída: 7 (um palíndromo possível: "dccaccd")
- Entrada: "a" → Saída: 1

**Complexidade de Tempo:** O(n), onde n é o comprimento da string.

**Complexidade de Espaço:** O(k), onde k é o número de caracteres distintos.
