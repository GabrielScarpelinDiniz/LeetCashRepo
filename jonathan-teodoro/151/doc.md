class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        print(words)

        l = 0
        r = len(words)-1


        while l<=r:
            words[l],words[r] = words[r],words[l]
            l +=1
            r-=1
        
        string = ''
        for i in range(len(words)):
            if words[i] == '':
                continue
            string += words[i]
            string += ' '
        
        return string[:-1]
            

Nesse exercício eu precisava inverter uma string removendo os espaços adicionais. Para solucionar a primeira coisa feita foi fazer um split separando por um espaço. Depois disso temos um array com palavras e spacos. Nesse array utilizo ponteiros em um loop for para invertê-lo. Depois de inferter, concateno as palavras em uma string. No final retorno a string menos o ultimo caracter que é um espaço.