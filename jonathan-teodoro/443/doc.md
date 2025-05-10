class Solution:
    def compress(self, chars: List[str]) -> int:
        
        currently = chars[0]
        value = 0
        s = ''
        for i in chars:
            if i == currently:
                value += 1
            else:
                if value == 1:
                    s += str(currently)
                else:
                    s += str(currently)
                    s += str(value)
                currently = i
                value = 1

        if value == 1:
            s += str(currently)
        else:
            s += str(currently)
            s += str(value)
        
        for i in range(len(s)):
            chars[i] = s[i]

        return len(s)

Hoje foi mais puxado. Fiz uma solucao pra cumprir que era ser O(N) em espaço extra. Havia feito uma solucao bem legal com hashmap mas optei por mudá-la para entrar nesse requisito. Aqui eu faço o seguinte. Vejo o primeiro item e o valor. 