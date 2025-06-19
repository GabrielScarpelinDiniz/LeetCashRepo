# Power of Four

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Power of Four é verificar se n é uma potência de 4

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o seguinte código: 

```php

function isPowerOfFour($n) {
    // Caso o valor seja igual 1 é retornado Verdadeiro
    if ($n == 1){
        return true;
    // Caso o valor seja menor que 1 é retornado Falso
    }else if($n < 1){
        return false;
    }

    // Retorna recursirvamente o valor da função de n dividido por 4
    return $this->isPowerOfFour($n / 4);
    }
```

## Complexidade
- Tempo: O algoritmo possui complexidade O($\log{n}$), onde n é o valor de n.

- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata53.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
