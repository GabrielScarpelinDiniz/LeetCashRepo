```python
class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        answer = []
        for i in range(1, len(height)):
            if height[i-1] > threshold:
                answer.append(i)
        return answer
``` 

Exercicio simples - criei um array auxiliar para guardar a resposta. Depois percorro o array pelo segundo valor e comparo com o anterior, se o anterior for menor que o threshold eu o adiciono no array auxiliar. No final de forma simples obtemos o array com os valores certos.