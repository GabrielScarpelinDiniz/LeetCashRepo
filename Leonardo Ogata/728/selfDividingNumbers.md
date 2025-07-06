# Self Dividing Numbers

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Self Dividing Numbers é encontrar todos os números em um intervalo que são divisiveis por todos os seus dígitos

&nbsp;&nbsp;&nbsp;&nbsp; Antes de apresentar esse código eu gostaria de pedir perdão a todos por esse crime que eu cometi, mas hoje eu não to batendo bem da cabeça. Eu não me orgulho disso e irei melhorar, espero que entendam.

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        # Array para armazenar a resposta
        arr = []    

        # Itera sobre os números no intervalo dado
        for i in range(left, right + 1):
            # Variável auxiliar para verificar se o número é divisível ou não
            div = True
            # Variável auxiliar para manipular o número
            auxI = i
            # Variável auxiliar para o método de iteração pelo número inteiro
            resto = 0
            # Itera sobre o número inteiro
            while auxI > 0:
                # Pega o último número do inteiro
                resto = auxI % 10
                # Atualiza o valor di número removendo o último digito
                auxI =  auxI//10
                # Caso o resto seja 0 ou o resto da divisão de i pelo resto seja diferente de 0 i não é divisível por esse número  
                if resto == 0 or i % resto != 0:
                    div = False
            # Caso ele seja divisível i é adicionardo ao array
            if div:
                arr.append(i)

        # Retorna o array
        return arr
```

## Complexidade
- Tempo: O algoritmo possui complexidade O($nlog_{n}$), onde n é o valor n.

- Espaço: O uso de espaço adicional é O(n).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata69😏.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
