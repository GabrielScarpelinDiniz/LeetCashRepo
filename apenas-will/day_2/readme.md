Esse problema consiste em achar o único número que não possui par em uma lista de elementos.

Para resolver esse problema, usei manipulação de bits. Em suma, realizei a operação de or exclusivo (XOR) em todos os elementos. Pela comutatividade e comportamento da operação, isso faz com que o resultado seja o número solitário.

Complexidade:
- Time complexity: $O(n)$
- Space complexity: $O(1)$