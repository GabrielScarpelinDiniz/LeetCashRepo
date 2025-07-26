/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let current = n;
    return function() {
        return current++;
    };
};

/** 
 * const counter = createCounter(10);
 * console.log(counter()); // 10
 * console.log(counter()); // 11
 * console.log(counter()); // 12
 */

 Aqui usamos closures para manter o estado entre chamadas. A função createCounter recebe n e cria uma variável current que guarda o número atual. Em seguida, retornamos uma função anônima que, quando chamada, devolve o valor atual e incrementa para a próxima chamada. Como closures em JavaScript “lembram” do escopo em que foram criadas, conseguimos preservar o valor de current entre as execuções. Isso nos permite criar um contador que começa em n e aumenta de 1 a cada chamada.