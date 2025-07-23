# Convert a Number to Hexadecimal

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Convert a Number to Hexadecimal é converter um número decimal para hexadecimal

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```python
def toHex(self, num: int) -> str:
        # Caso Base
        if num == 0:
            return "0"

        # Se o número for negativo, converte para valor positivo de 32 bits
        if num < 0:
            num = (1 << 32) + num
    
        # Retorna o número convertido para hexadecimal 
        return convertToHex(num)

# Função de conversão de decimal para hexadecimal
def convertToHex(num: int) -> str:
    # Dicionário que mapeia números de 10 a 15 para suas representações hexadecimais
    dic = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    
    # String que vai armazenar o resultado hexadecimal
    hexa = ""
    
    # Loop para conversão para hexadecimal
    while num > 0:
        # Pega o resto da divisão do número por 16 
        temp = num % 16

        # Se o resto for menor que 10 adiciona o dígito 
        if temp < 10:
            hexa += str(temp)
        else:
            # Se o resto for 10 ou maior usa o dicionário para adicionar a letra 
            hexa += dic[temp]
        
        # Atualiza o valor de num
        num = num // 16

    # Retorna a string do número hexadecimal invertida 
    return hexa[::-1]
```

## Complexidade
- Tempo: O algoritmo possui complexidade O($\log{n}$), onde n é o tamanho de num.

- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata87.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
