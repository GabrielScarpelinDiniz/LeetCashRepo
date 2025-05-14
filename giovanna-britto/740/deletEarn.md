# Dia X de LeetCash

Acho que já provamos para nós mesmos que somos capazes, podemos nos dar por vencidos e encerrar a competição, não é mesmo!? Quem eu quero enganar? Ninguém desistir disso mesmo... Pois é, pelo menos eu me recuperei da minha doenção, agora me encontro bem e recuperada, mas como não é novidade para ninguém, continuo usando DP para resolver esse negócio.

Dessa vez, o exercício que eu escolhi foi o 740, Delete and Earn. A ideia do problema é bem parecida com o House Robber: você precisa escolher números de uma lista para ganhar pontos, mas ao escolher um número `n`, você é obrigado a eliminar todos os `n - 1` e `n + 1` da lista.

Aqui vai o passo a passo do que eu fiz:

1. Verifico se a lista está vazia. Se estiver, retorno 0.
2. Encontro o maior número da lista para definir o tamanho do array `points`, que vai armazenar quanto de “ponto” eu ganho ao escolher cada número.
3. Preencho o array `points`, somando os valores correspondentes (por exemplo, se tem três `3`, somo `3 + 3 + 3 = 9` e coloco em `points[3]`).
4. Crio o array `dp` para aplicar programação dinâmica (igual ao House Robber). A lógica é decidir se compensa pegar o número atual ou pular ele.
5. Retorno o último valor de `dp`, que contém a resposta final.

Por hoje é isso, obrigada pela atenção!!!