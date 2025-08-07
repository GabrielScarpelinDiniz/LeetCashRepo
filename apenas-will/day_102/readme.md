## Exercício: 19. Remove Nth Node From End of List
**Objetivo**: Dado uma lista ligada e um inteiro `n`, remova o n-ésimo último elemento da lista e retorne o início da lista.

## Descrição geral da estratégia
Para resolver crio três ponteiros os quais indicarão o elemento que será eliminado, o elemento anterior ao que será eliminado e um elemento de espaçamento. A ideia é que a distância entre o elemento de espaçamento e o elemento que será eliminado seja de tamanho `n` e, com isso, ao posicionar o elemento de espaçamento na última posição da lista, seremos capazes de eliminar o elemento correto da lista ligada. Para isso, primeiro ando com o ponteiro do elemento de espaçamento $n-1$ vezes. Em seguida, ando todos os três ponteiros uma posição por vez a cada iteração do loop principal até que o elemento de espaçamento seja nulo. Quando isso ocorre, o elemento anterior recebe como seguinte o elemento posterior ao elemento que será eliminado. Após isso o elemento que seria eliminado tem seu valor atualizado para nulo (o que fará com que ocorra sua exclusão na próxima passagem do _garbage collector_ do Java). Caso `n` seja igual ao comprimento da lista, retorna-se o elemento seguinte ao elemento anterior. Caso contrário, retorna-se o primeiro elemento original da lista.

## Análise de complexidade
Para uma lista ligada com $n$ nós, tem-se:
- **Time complexity**: $O(n)$ 
- **Space complexity**: $O(1)$
