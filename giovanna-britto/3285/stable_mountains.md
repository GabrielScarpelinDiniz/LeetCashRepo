# Mais um dia de LeetCash

Hoje eu resolvi o exercício 3285, no qual pedia assim:

> Há n montanhas em uma fileira, e cada montanha tem uma altura. Você recebe uma matriz de inteiros heightonde height[i]representa a altura da montanha ie um inteiro threshold.

> Uma montanha é considerada estável se a montanha imediatamente anterior ( se existir ) tiver uma altura estritamente maior que threshold. Observe que a montanha 0 não é estável.

> Retorna uma matriz contendo os índices de todas as montanhas estáveis ​​em qualquer ordem.


Para resolver isso eu segui os seguintes passos:

1. Criei uma lista `montanha` que armazena as montanhas estáveis;
2. Tenho um for para iterar sobre a lista de alturas das montanhas;
3. Tenho um if para comparar se a altura da montanha anterior é maior que o inteiro `threshold`, caso seja adiciono o valor do indice da montanha no array
4. Retorno o array de montanhas

E pronto! Mais um exercício resolvido!!!
 

