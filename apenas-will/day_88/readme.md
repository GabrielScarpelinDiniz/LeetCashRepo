## Exercício: 1721. Swapping Nodes in a Linked List
**Objetivo**: Dada uma lista ligada e um inteiro $k$, troque o k° primeiro e último elementos da lista e retorne a cabeça da lista.

## Descrição geral da estratégia
Para resolver crio 4 variáveis que armazenarão os nós a serem trocados e os nós anteriores aos primeiros. Para tal, começo encontrando o primeiro elemento a ser trocado e seu antecessor iterando pela lista até alcançar a posição $k$. Em seguida, para achar os dois últimos, crio um ponteiro auxiliar que marca a distância até o fim, chamando-o `end`, e itero pela lista até seu final, incrementando a posição da variável que armazena o segundo elemento a ser trocado e seu respectivo antecessor. Com essas 4 variáveis encontradas, faço a substituição, determinando que o antecessor do primeiro receba como próximo o segundo e vice-versa. Ajusto também as outras trocas, fazendo com que os elementos posteriores àqueles que foram trocados sejam sejam também trocados (para manter as outras posições da lista). Por fim, lido com os casos de borda conferindo o tamanho da lista (determinado através do número de execuções do loop principal). Caso o comprimento da lista seja igual ao valor $k$, retorno o primeiro elemento trocado. Caso $k$ seja 1 retorno o segundo valor trocado. Caso contrário, retorno a cabeça original da lista.

## Análise de complexidade
Para uma lista com $n$ nós, tem-se:
- **Time complexity**: $O(n)$ 
- **Space complexity**: $O(1)$
