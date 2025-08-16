## Exercício: 557. Reverse Words in a String III
**Objetivo**: Dado uma string, retorne a string com suas palavras invertidas.

## Descrição geral da estratégia
Para resolver uso um `StringBuilder` que armazena o resultado final e um que armazena as palavras encontradas pouco a pouco. Nesse contexto, itero pela string, salvando suas palavras no `StringBuilder` temporário. Ao encontrar um espaço, insiro essa palavra de trás para frente no `StringBuilder` de resultado. Faço isso até o final da string, retornando o resultado ao final.

## Análise de complexidade
Para uma string com $n$ caracteres, tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(n)$
