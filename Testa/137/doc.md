Assim como o single number I a ideia desse exercício é encontrar o número que está sozinho, porém, nesse caso ao invés de duplas nós temos trios e apenas um número sozinho. Aqui não funciona a técnica do XOR aplicada uma única vez.
Nesse exercício eu resolvi com Nlog(N) fazer uma simples verificação.
Primeiro eu ordeno a lista em log(N) operações e depois eu vou observando número a número. Eu pego o indice i e olho se o indice i+2 tem o mesmo valor.
Enquanto documentava eu descobrir a solução perfeita, eu e meu colega de quarto aplicamos duas vezes o XOR na lista e consequentemente o resultado foi o valor que está sozinho

No final a solução que submeti foi a de Nlog(N)

Essa foi bem trivial 

![Trivial](trivial.jpg)

Assinado
por: [Vinicius Testa Passos](https://www.linkedin.com/in/vinicius-testa-passos/)