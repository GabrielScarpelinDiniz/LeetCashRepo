var fibGenerator = function*() {
    let a = 0;
    let b = 1;
    while(true){
        yield a;
        [a, b] = [b, a + b];
    }
};

Este problema pode ser resolvido de forma elegante usando uma função geradora. Em uma entrevista, eu explicaria que essa abordagem é ideal porque gera os números de Fibonacci sob demanda, usando a palavra-chave yield. Isso significa que, em vez de criar um array gigante, a função pausa e retorna um valor a cada chamada do .next(), o que é muito mais eficiente em termos de memória. A solução é simples: inicializamos as duas primeiras variáveis da sequência, e um loop infinito se encarrega de calcular e retornar o próximo número a cada iteração, mantendo o estado entre as chamadas.