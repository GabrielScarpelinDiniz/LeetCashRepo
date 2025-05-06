## Exercício: 2. Add Two Numbers
**Objetivo**: Dada duas listas ligadas que representas inteiros de trás para frente ( a lista [1] -> [2] -> [3] representa o número 321), gere uma lista ligada que armazena a soma desses dois inteiros;

## Descrição geral da estratégia
Para resolver, basicamente empreguei o algoritmo padrão de soma. Nesse sentido, gerei uma variável `rest` que armazena o que sobrar a soma e que deve ser passado adiante (9 + 9 = 18. Rest = 1, que vai ser passado adiante). Após isso, foi necessário ir somando os dois valores com o `rest`, conferindo se esse valor passava ou não de 10. Caso passasse, na soma seguinte eu acrescia o valor 1, caso contrário, era só armazenar o resultado dessa soma no nó da lista de resultado.

## Análise de complexidade
Para um inteiro com $n$ algarismos (o maior, caso os inteiros tenham tamanhos distintos), tem-se:
- **Time complexity**: $O(n)$
- **Space complexity**: $O(n)$
