# Dia 25 de Leet Cash?

Já me perdi na contagem de dias, então é isso que teremos para hoje!! Eu acabei de descobrir que não havia feito o algoritmo de busca binária então mais uma vez, é isso que teremos para hoje!!!

Como de costume, dado uma lista de números eu devo encontrar o índice do target, ou então -1 se o target não for encontrado na lista. Para resolver isso eu segui o padrão:

1. Crio a variável `mid`, para guardar o meio do array
2. Crio a variável `esq`, inicializada com 0
3. Crio a variável `dire`, que armazena o tamanho do array -1
4. For para iterar sobre o array:
    - Se `nums[i] == target`, significa que eu achei o target, então retorno o índice `i`
    - Se `nums[i] < mid`, então direita recebe o meio -1
    - Se `nums[i] > mid`, então esquerda recebe o meio +1

5. Caso ao final da execução o target não seja igual o meio, significa que não achei o target, então retorno -1.

Pronto! Exercício resolvido, até amanhã!!!