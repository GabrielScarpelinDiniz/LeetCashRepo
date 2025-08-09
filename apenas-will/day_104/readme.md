## Exercício: 151. Reverse Words in a String
**Objetivo**: Dada uma string, inverta a ordem das palavras dessa string. Caso hajam espaços repetidos entre as palavras ou no início/final da string, eles devem ser removidos.

## Descrição geral da estratégia
Para resolver utilizo uma estratégia de duplo ponteiro (slow/fast com reset/catch-up). Para isso, começo adicionando dois ponteiros no final da string. Um deles, o ponteiro rápido, anda 1 posição à cada iteração do loop principal, enquanto o segundo, o lento, apenas se movimenta em situações específicas. Ambos os ponteiros andam 1 posição em direção ao início da string caso ambos estejam sobre um caracter de espaço. Caso ambos estejam sob um caracter diferente de um espaço, então apenas o rápido anda uma posição. Porém, caso o caracter na casa do ponteiro rápido seja um espaço enquanto na posição do caracter devagar não seja, então significa que achamos uma palavra (a sequência de caracteres em `fast + 1` e `slow + 1`). Com a palavra em mãos, utilizo um loop secundário que a adiciona na variável `res`. Após o fim do processo anterior, é realizado um tratamento para adicionar a última palavra (caso ela tenha sido omitida) ou remover um espaço adicional (caso ele tenha sido adicionado). Após isso, retorna-se a variável `res`.

## Análise de complexidade
Para um string com $n$ caracteres, tem-se:
- **Time complexity**: $O(n)$ ( $\Theta(2n)$ ) 
- **Space complexity**: $O(n)$
