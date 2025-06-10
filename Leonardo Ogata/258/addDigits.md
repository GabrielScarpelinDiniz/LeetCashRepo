# Add Digits

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema addDigits é somar os digitos de um número até que o número possua apenas um caractere. Sim eu sei que parece muito fácil e na verdade é mesmo, porém eu tive que passar uma meia hora pesquisando pra descobrir como faz isso com a complexidade O(1)

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Se o número for menor que 9 ele é retornado
        if num <= 9:
            return num
        # Caso o contrário é aplicada a fórmula da raiz digital
        else:
            return 1 + (num - 1) % 9
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(1).

- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata35.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
