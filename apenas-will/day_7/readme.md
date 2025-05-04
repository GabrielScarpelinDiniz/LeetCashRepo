## Exercício: 345. Reverse Vowels of a String
**Objetivo**: Dada uma string, inverta as vogais em ordem de aparição (trocar primeira vogal com a última, a segunda com a penúltima e assim por diante);

## Descrição geral da estratégia
Coloquei um ponteiro no início da string e um no final, então fui aproximando os dois. Caso eu encontre duas vogais, inverto as duas, caso contrário, só aproximo mais os dois. Ps. gostei desse exercício porque, apesar de simples, me obrigou a usar o `StringBuilder` do java.

## Análise de complexidade
Para uma string com $n$ caracteres, tem-se:
- **Time complexity**: $O(n)$, $\Theta(\frac{n}{2})$ 
- **Space complexity**: $O(n)$, (por causa do StringBuilder)

## OBS:
Se alguém ler esta documentação e souber se existe alguma linguagem em que o `string` é um datatype dinâmico, por favor, me manda mensagem.
