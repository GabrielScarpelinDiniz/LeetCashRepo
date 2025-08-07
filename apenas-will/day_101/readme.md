## Exercício: 551. Student Attendance Record I
**Objetivo**: Dado uma string que representa as presenças de um estudante durante um certo período ("P" indica que ele estava presente, "A" que estava ausente e "L" que estava atrasado), determine se esse aluno é elegível para um prêmio. Para ser elegível para o prêmio, o aluno deve ter menos de 2 faltas totais e menos de 3 atrasos consecutivos.

## Descrição geral da estratégia
Para resolver crio duas variáveis que armazenam a quantidade de faltas e de atrasos. Em seguida, itero pela string conferindo seus caracteres. Se um "L" for encontrado, incremento em um sua contagem. Se um "A" for encontrado, incremento sua contagem e zero a contagem de "L". Se qualquer outra letra ("P") for encontrada, zero a contagem de "L". A cada iteração do loop, confiro se a contagem de "A" é igual a 2 ou se a quantidade de "L" é igual à 3, retornando `false` caso a condição seja satisfeita. Por fim, após todas as iterações do loop, retorno `true`.

## Análise de complexidade
Para uma string com $n$ caracteres, tem-se:
- **Time complexity**: $O(n)$ 
- **Space complexity**: $O(1)$
