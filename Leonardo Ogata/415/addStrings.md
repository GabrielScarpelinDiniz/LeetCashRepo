# Add Strings

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Add Strings é somar duas strings sem converter elas para int diretamente

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
    def addStrings(self, num1: str, num2: str) -> str:
        # Dicionário para atribuir valores as strings
        dic = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

        # Define tamanho da maior string
        size = max(len(num1), len(num2))

        # Array para armazenar valores de num1
        arrNum1 = []
        # Array para armazenar valores de num2
        arrNum2 =[]

        # Itera sobre as strings de trás para frente começando do maior valor
        for i in range(size -1, -1, -1):
            # Caso o indice exista na string o caractere é adicionado ao array
            if i < len(num1):
                arrNum1.append(num1[i])
            # Caso o indice exista na string o caractere é adicionado ao array
            if i < len(num2):
                arrNum2.append(num2[i])
        
        # Define qual array possui  o maior e o menor comprimento
        if len(arrNum1) < len(arrNum2):
            smallest = arrNum1
            biggest = arrNum2
        else:
            smallest = arrNum2
            biggest = arrNum1
        
        # Preenche o menor array com 0 para igualar o tamanho do maior
        while len(smallest) < len(biggest):
            smallest.append("0")

        # Armazena resto da soma
        carry = 0   
        # Armazena resposta
        ans = ""

        # Itera pelos arrays somando seus valores
        for i in range(len(arrNum1)):
            # Somatório dos itens + o resto da soma
            summer = dic[arrNum1[i]] + dic[arrNum2[i]] + carry

            # Caso o valor da soma dos caracteres seja menor que 10 o caractere de soma é adicionado a string de resposta e o resto é zerado
            if summer < 10:
                ans += str(summer)
                carry = 0
            # Caso o valor da soma dos caraceteres seja maior que 10 o último caracetere da soma é adicionado a resposta e os outros caracteres se tornam o resto da soma
            else: 
                ans += str(summer % 10)
                carry = summer // 10
        
        # Caso após a última iteração ainda exista um valo de resto ele é adicionado
        if carry != 0:
            ans += str(carry)
        
        # Retorna a string ao contrário
        return ans[::-1]
```

## Complexidade
- Tempo: O algoritmo possui complexidade O(n + m), onde n é o tamanho de num1 e m é o tamanho de m.

- Espaço: O uso de espaço adicional é O(n).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata73.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
