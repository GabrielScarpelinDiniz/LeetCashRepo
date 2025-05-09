# Mais um dia de Leet Cash

Oii gente, hoje é dia 08 de maio de 2025, ainda faltam 190 dias para o fim da temporada e eu não vejo a hora disso acabar... Como agora, no sexto módulo de CC, estamos vendo programação dinâmica, estou me desafiando a aplicar o que aprendemos na aula. Sendo assim, eu resolvi o exercício 746. 

Esse exercício considera uma entrada ``cost`, que é um array em que cada índice do array representa o degrau de uma escada, e o valor desse index é o custo para subir nesse degrau, então você tem duas opções sobe 1 degrau ou pula para o de cima, de forma que você chegue até o final com o menor custo possível. Para resolvir isso meu algoritmo segue a seguinte ordem:

1. Define a variável `n` como o tamanho do array `cost`
2. Cria o array `dp` zerado e do mesmo tamanho do array de custo. 
3. Define para a posição 0 o custo dessa posição;
4. Define para a posição 1 o custo desse degrau;
5. A partir disso, tem um for que começa a iterar a partir do terceiro degrau (degrau 0 e 1 já definidos) e vai até o valor de n
    6. No for a posição do índice em i recebe o valor do custo daquele degrau somado com o mínimo entre i-1 e i-2, isso faz com que o algoritmo decida se compensa subir 1 ou dois degraus e mantenha a lógica do algoritmo. O valor de cada posição demonstra a soma final daquele degrau.

7. Por fim, o algoritmo retorna o mínimo entre ir para o último a partir do penúltimo degrau ou do antepenúltimo. 

Assim o algoritmo resolve o problema com uma complexidade $O(n)$ e memória $O(n)$. Então é isso, muito obrigada pela atenção!!