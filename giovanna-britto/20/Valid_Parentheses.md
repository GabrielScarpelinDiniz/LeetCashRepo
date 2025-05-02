# Quinto dia de Leet Cash

Seguinte, ontem teve churrasco no Share, ficamos até 01h da manhã (deu tempo até de jogar Twister), o problema é, estava um vento e um frio insuportável, o resultado? Estou doente agora! Porém, um desafio é um desafio...

Hoje eu resolvi o desafio número 20, no qual, dado uma string `s`, contendo `()` ou `{}` ou `[]`, você deveria dizer se ela é `true` ou `false`, caso você abrisse e fechasse um parenteses. 

Para resolver isso, eu segui as seguintes etapas de desenvolvimento:

1. Cria uma pilha (para armazenar um dos caracteres de abertura);
2. Cria um dicionário, para armazenar qual o valor (caractere de fechamento) correspondente da chave armazenada (caractere de abertura);
3. For para iterar sobre a String;
4. Dentro do laço há um if:
    - Caso haja um caractere de abertura, ele empilha na pilha(`pilha.push(s[i])`);
    - Caso não seja um de fechamento, verifica se
        - O topo da pilha é diferente do item `s[i]` contido no dicionário, se diferente retorna `false`;
5. Após o fim das iterações, é retornado se o tamanho da pilha é zero, caso sim retorna `true`, caso não retorna `false`.

Mais um exercício resolvido! Caso tenha dúvidas...
[Sim, Eu duvido de Você Giovanna!](https://docs.google.com/document/d/1yg95tsyo0keXi2wp5q__NHhtKiTTOGZ4MhzTV1Rzr6E/edit?usp=sharing)