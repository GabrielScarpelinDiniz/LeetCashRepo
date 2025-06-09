## Exercício: 997. Find the Town Judge
**Objetivo**: Dada uma lista de relações de confiança (lista com $n$ elementos na qual $n[i]=[a_i,b_i]$, indicado que o indivíduo $a_i$ confia no indivíduo $b_i$) determine quem é o "_juiz da cidade_" (indivíduo que não confia em ninguém mas que todos confiam);

## Descrição geral da estratégia
Para resolver gero uma lista de listas com dois elementos. O primeiro elemento numa determinada posição $i$ representa a quantidade de pessoas que o indivíduo $i$ confia, enquanto o segundo representa quantas pessoas confiam nesse indivíduo. Em seguida, itero pela lista de confiança, incrementando na lista gerada as quantidades de pessoas que confiam em um indivíduo e de pessoas que um indivíduo confia. Após isso, itero pela lista de contagem e, quando encontro um elemento que confia em 0 indivíduos e que possui a confiança de todos os outros indivíduos, retorno esse elemento. Caso contrário, retorno -1.

## Análise de complexidade
Para uma lista com $c$ confianças e $n$ indivíduos, tem-se:
- **Time complexity**: $O(c)$ 
- **Space complexity**: $O(n)$

