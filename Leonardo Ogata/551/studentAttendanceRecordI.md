# Student Attendance Record I

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Student Attendance Record I é definir se um aluno pode ser aprovado ou não. Um aluno só pode ser aprovado caso ele não tenha mais de 2 faltas (A) totais e mais de 3 atrasos (L) consecutivos.

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
    def checkRecord(self, s: str) -> bool:
        # Conta atrasos
        late = 0
        # Conta Faltas
        absent = 0

        # Itera sobre a lista
        for i in s:
            # Aumenta a contagem de atrasos
            if i == 'L':
                late += 1
            # Aumenta a contagem de faltas e zera a streak de atrasos
            if i == 'A':
                late = 0
                absent += 1
            # Zera a streak de atrasos
            if i == 'P':
                late = 0
            # Caso os atrasos sejam iguais a 3 ou faltas igual a 2 o aluno é reprovado 
            if late == 3 or absent == 2:
                return False
        # O aluno é aprovado
        return True
```

## Complexidade
- Tempo: O algoritmo possui complexidade O($n$), onde n é o tamanho da string s.

- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata101.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
