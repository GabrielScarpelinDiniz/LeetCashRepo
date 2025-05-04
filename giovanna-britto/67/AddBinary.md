# Sexto dia de Leet Cash

Bom, eu continuo doente, sigo fazendo isso com nariz entupido, garganta inflamada e dor de cabeça. E hoje, dia 03 de maio, já temos dois que estão com 1 dia a menos na competição.

Como minha cabeça está doendo muito não documentarei dignamente, então segue um psedocódigo do meu código:

    função somarBinarios(a, b):
        inicializa ponteiro i no final de a 
        inicializa ponteiro j no final de b 
        inicializa variável auxiliar 
        inicializa resultado como lista vazia

        enquanto i >= 0 ou j >= 0 ou carry != 0:
            se i >= 0:
                valorA = valor inteiro de a[i]
            senão:
                valorA = 0

            se j >= 0:
                valorB = valor inteiro de b[j]
            senão:
                valorB = 0

            soma = bitA + bitB + carry
            resultado_adicionado = soma % 2      
            auxiliar = soma // 2                    

            adicionar resultado_adicionado ao início de resultado

            Decrementa i e j

        retorna resultado como string

É isso Gente, desculpa pela qualidade, foi o que deu...