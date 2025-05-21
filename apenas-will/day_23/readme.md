## Exercício: 125. Valid Palindrome
**Objetivo**: Dada uma string, determine se é um palíndromo (palavra ou frase que é igual de trás para frente e de frente para trás);

## Descrição geral da estratégia
Para resolver, eliminei todos os caracteres não alfa-numéricos (sinais de pontuação e espaços), coloquei a string inteira em minúsculo e iterei por ela com dois ponteiros. Caso o caracter na posição descrita pelo ponteiro da frente fosse diferente daquela do ponteiro de trás, o algoritmo retorna `false`.

## Análise de complexidade
Para uma string com $n$ caracteres, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(1)$ 