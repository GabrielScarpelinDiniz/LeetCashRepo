class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)  
        count = 0
        for stone in stones:
            if stone in jewel_set:
                count += 1
        return count

Exercicio facil pq to dodoi. Utilizando set fica facil.  Ele transforma as joias em um conjunto (pra procurar mais rápido) e percorre todas as suas pedras, somando 1 cada vez que encontra uma pedra que também é uma joia. No fim, retorna esse total.