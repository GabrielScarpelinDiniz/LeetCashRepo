# Convert the Temperature

&nbsp;&nbsp;&nbsp;&nbsp; O objetivo do problema Convert the Temperature é retornar a temperatura celsius convertida para kelvin e fahrenheit.

&nbsp;&nbsp;&nbsp;&nbsp; Para isso desenvolvi o primeiramente o seguinte código: 

```python
    def convertTemperature(self, celsius: float) -> List[float]:
        # Converte temperatura para celsius
        kelvin = celsius + 273.15
        # Converte temperatura para fahrenheit
        fahrenheit = (celsius * 1.80) + 32.00

        # Retorna as temperaturas convertidas
        return [kelvin, fahrenheit]
```

## Complexidade
- Tempo: O algoritmo possui complexidade de aproximadamente O(1).
- Espaço: O uso de espaço adicional é O(1).

<div style="display: flex; align-items: center; justify-content: center;">
    <img src="leoogata81.jpg" alt="leoogata" style="width: 300px; height: auto; margin-right: 20px;">
    <div>
        <p>Meu nome é Leonardo Ogata e essa foi minha master class, muito obrigado a todos, vejo vocês amanhã!</p>
    </div>
</div>
