# Quarto dia de LeetCash

Hoje é dia primeiro de maio, feriado do dia do trabalhador, e eu estou o quê? TRABALHANDO!!!! Mas tudo pela competição...

Segue mais um desafio nível easy (prometo que vou melhorar galerinha, mas é que tem churrasco hoje!). Eu resolvi o exercício número 13. Roman to Integer, em que dada uma entrada s eu deveria converter o número romano em inteiro, então eu segui os seguintes passos de execução:

1. Crio um dicionário `valorRomano`, para armazenar o algarismo romano e o seu valor como inteiro.
2. Crio uma variável para armazenar a soma total, chamada `total`, e outra chamada `bau` para armazenar o último valor do número romano e usar como comparativo.
3. Faço um laço for para iterar sobre a entrada de trás para frente (números romanos são lidos de trás para frente), dentro do for há:
    - Variável `atual` para armazenar o valor da variável do algarismo romano;
    - If para comparar se `atual` é menor que `bau`, caso sim, subtrai o valor do total, caso não soma o valor com total;
    - Variável bau recebe o valor de atual e o laço segue a iteração
4. Ao final da iteração, é retornado o valor total.

Pronto, exercício resolvido!! Caso tenha dúvidas da minha submisão segue o docs:
[Sim, Eu duvido de Você Giovanna!](https://docs.google.com/document/d/1yg95tsyo0keXi2wp5q__NHhtKiTTOGZ4MhzTV1Rzr6E/edit?usp=sharing)