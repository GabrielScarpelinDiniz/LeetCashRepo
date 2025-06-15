Primeiro, percorremos a lista e registramos essa contagem em um dicionário. Depois, olhamos nesse dicionário para encontrar os dois números que aparecem exatamente duas vezes e os adicionamos na resposta.

```python
class Solution:
    def getSneakyNumbers(self, nums):
        freq = {}      
        result = []    
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for num in freq:
            if freq[num] == 2:
                result.append(num)

        return result
```







