## Exercício: 455. Assign Cookies
**Objetivo**: Dado um array que indica a fome de um grupo de crianças e um array com o tamanho de uma série de cookies, determine quantas crianças podem ser satisfeitas distribuindo os cookies (uma criança se sente satisfeita se ela receber um cookie maior ou igual ao tamanho da sua fome).

## Descrição geral da estratégia
Para resolver uso uma abordagem gulosa (irônico, não?) que distribui os menores cookies para as crianças com menos fome e vai, progressivamente, avançando para as crianças com mais fome. Primeiramente, ordeno os arrays de crianças e cookies. Em seguida, tento assinalar o primeiro cookie à primeira criança. Caso o cookie seja maior ou igual à fome dessa criança, incremento uma variável de resultado em 1. Caso contrário, tento com o próximo cookie. O processo anterior continua até que os cookies ou crianças tenham acabado. Por fim, retorno o valor armazenado na variável de resultado.

## Análise de complexidade
Para um array com $n$ crianças e outro com $m$ cookies, tem-se:
- **Time complexity**: $O(\log(n^nm^m))$ 
- **Space complexity**: $O(1)$
