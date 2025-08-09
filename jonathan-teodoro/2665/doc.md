A função cria um contador encapsulado num closure, guardando o valor atual (value) e o inicial (init). Ela retorna um objeto com três métodos: increment soma 1, decrement subtrai 1 e reset volta ao valor inicial. Isso garante que o estado do contador seja controlado de forma privada.

/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let value = init;
    return {
        increment: () => ++value,
        decrement: () => --value,
        reset: () => (value = init)
    };
};


/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */