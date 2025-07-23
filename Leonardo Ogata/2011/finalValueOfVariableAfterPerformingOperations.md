# Final Value of Variable After Performing Operations

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Final Value of Variable After Performing Operations é reconhecer uma linguagem que possui apenas 4 operações, sendo elas ``++X``, ``X++``, que incrementa 1 à variável, e ``--X``, ``X--`` que decrementa 1 da variável, e retornar o valor de x após as operações

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o primeiramente o seguinte código: 

```python
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # Variável para receber valor da resposta
        x = 0

        # Itera sobre array de operações
        for i in operations:
            # Caso a operação seja subtrair é subtraido um da variável de resposta
            if i == "--X" or i == "X--":
                x -= 1
            # Caso o contrário é incrementado um à variável de resposta
            else:
                x += 1
        
        # retorna a respota
        return x
```

## Complexidade
- Tempo: O algoritmo possui complexidade de aproximadamente O(n), em que n representa o tamanho do array de operações.
- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata84.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
