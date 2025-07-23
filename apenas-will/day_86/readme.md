## Exercício: 234. Palindrome Linked List
**Objetivo**: Dada uma lista ligada, determine se ela é um palíndromo (é igual a ela mesma de trás para frente).

## Descrição geral da estratégia
Para resolver, adiciono todos os nós da lista ligada em uma lista convencional. Em Seguida, usando 2 ponteiros, itero pela lista conferindo se o último elemento é igual ao primeiro, o penúltimo é igual ao segundo e assim por diante. Caso seja encontrado um par que não seja igual, retorno `false`. Caso contrário, itera-se até o meio da lista e retorna-se `true`.
   
## Análise de complexidade
Para uma lista ligada com $n$ nós, tem-se:
- **Time complexity**: $O(n)$ 
- **Space complexity**: $O(n)$ 