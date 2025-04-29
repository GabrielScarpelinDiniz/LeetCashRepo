Bom dia perdedores! Como vocês estão? 

Dessa vez eu não tão fodástico :(

Dito isso, mais um dia concluindo a missao!!

Decidi realizar o desafio do palíndromo hoje. A resolução dele pode ser feita de outra maneira, utilizando operações de resto, etc.. Resultando em uma complexidade e menor tempo de execução. Entretanto, no dia de hoje optei por treinar meus conhecimentos em pilhas (utilizando python dessa vez). 

```python
    class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        stack = []        

        if x<0:
            return False

        for i in str(x):
            stack.append(i)

        for i in stack:
            poped = stack.pop()
            if i != poped:
                return False

        return True   
        

```

A resolução foi a seguinte, primeiro converto o número to string e, depois, adiciono cada caracter em uma pilha (Resolução fraca, eu sei)

Depois disso, eu percorro a pilha comparando o item percorrido com o ultimo da pilha. Se for diferente, acabamos por ai - Não é palindromo. Se for igual, nós seguimos até finalizar o array ou aparecer uma dupla entre primeiro e ultimo diferentes.

Gostei da minha resolução? Não, mas seguimos!

Lets bora 2/200 - se preparem perdedores.

![alt text](image.png) 

mood de hoje