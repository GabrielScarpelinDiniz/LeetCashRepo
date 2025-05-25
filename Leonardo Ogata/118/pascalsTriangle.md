# Pascal's Triangle

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Pascal's Triangle é receber um valor de coluna e gerar as colunas do triângulo de pascal até esse número

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
 def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        #Retorna os casos base
        if numRows == 0:
            return []

        if numRows == 1:
            return [[1]]

        # Cria os casos base da pirâmide
        piramid = [[1], [1, 1]]

        # Inicia a próxima coluna da pirâmide
        x = 2

        # Loop enquanto a coluna final não for escrita
        while x < numRows:
            # Cria nova coluna
            newRoll = [0] * (x + 1)
            # Define o primeiro e último número
            newRoll[0] = 1
            newRoll[-1] = 1

            # Preenche a pirâmide através de Programação Dinâmica
            for i in range(1, len(newRoll) - 1):
                newRoll[i] = piramid[x-1][i-1] + piramid[x-1][i]
            piramid.append(newRoll)

            # Avança para a próxima coluna
            x += 1
        
        # Retorna a piramide criada
        return piramid
```

## Complexidade
- Tempo: O algoritmo possui complexidade de aproximadamente O($n^2$), onde n é o tamanho da entrada.
- Espaço: O uso de espaço adicional é O(${n^2}$), devido a tabela PD criada.

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata27.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
