## Exercício: 1275. Find Winner on a Tic Tac Toe Game
**Objetivo**: Dadas uma array que representas movimentos de um jogo da velha, determine o vencedor (considere o jogador "A" como o primeiro a jogar e "B" como o segundo);

## Descrição geral da estratégia
Para resolver primeiro armazeno o resultado dos movimentos no tabuleiro do jogo, adicionando "A" ou "B" com base no jogador que fez o movimento. Em seguida, testo, nesta ordem, se alguém venceu por ter completado a linha, se alguém venceu por ter completado a coluna, se alguém venceu por ter completado a diagonal principal e se alguém veneu por ter completado a diagonal secundária. 

## Análise de complexidade
Para um array com $n$ jogadas, tem-se:
- **Time complexity**: $O(n)$ 
- **Space complexity**: $O(1)$ (sempre se salva um tabuleiro com 9 posições)