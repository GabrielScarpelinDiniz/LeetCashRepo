# Number of Employees Who Met the Target

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Number of Employees Who Met the Target é retornar quantos trabalhadores do array hours bateram a meta target.

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o primeiramente o seguinte código: 

```python
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        # Armazena quantos trabalhadores bateram a meta de horas
        counter = 0

        # Itera sobre o array de horas
        for i in hours:
            # Se o valor das horas for igual o maior que o target o contador é incrementado
            if i >= target:
                counter += 1
        
        # Retorna o contador
        return counter
```

## Complexidade
- Tempo: O algoritmo possui complexidade de aproximadamente O(n), em que n é o tamanho do array hours.
- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata96.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
