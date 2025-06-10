class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        return [kelvin, fahrenheit]

exercicio ridiculo pq tava esquecendo. so uma conversaozinha basica, celsius para celsius e farehnheit, matematica basica bem trivial, depois retorno a lista com ambos valores.