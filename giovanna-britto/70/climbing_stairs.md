# Outro dia de Leet Cash

Olá gente! Espero que vocês se encontrem bem hoje, porque depois de resolver esse exercício usando programação dinâmica em 10 minutos fez o meu dia. Além disso, hoje, dia 09 de maio de 2025, tivemos o onboarding do Inteli Academy - o que marca um novo período da minha vida (Blockchain jamais te abandonarei), o que contribuiu para a minha felicidade de hoje, o que significa que não irei reclamar da competição hoje!!!

O Exercício de hoje consistia em dizer quantas possibilidades existiam para subir uma quantidade de degraus na escada, para isso eu resolvi o exercício seguindo a seguinte lógica:

1. Declarei casos bases usando condicionais, então se `n == 1` retorna 1 e se `n == 2` retorna 2. Isso é importante, porque eu só tenho uma opção para subir o primeiro degrau, e só tenho duas opções para subir o degrau 2 (sobe 1 e depois sobe outro, ou então pula 1, o que é duas opções);
2. Criei um array `possibilidades` de tamanho n (quantidade de degraus na escada), e atribui como valor 0 as posições;
3. Atribui ao degrau 1 a possibilidade 1 e atribui ao degrau 2 a possibilidade 2 (marca o início do algoritmo);
4. Laço de repetição que itera a partir do terceiro degrau até o último, e adiciona na posição do degrau a possibilidade sendo a soma do valor da última posição com o valor da penúltima posição;
5. Depois eu retorno o valor da possibilidade no degrau n-1, já que o array começa a contar do 0. 

E assim temos mais um exercício resolvido usando programação dinâmica!!! Muito obrigada pela atenção.