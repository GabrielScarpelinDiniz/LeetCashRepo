/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    let chamado = false;
    let resultado;

    return function(...args){
        if(!chamado){
            resultado = fn(...args);
            chamado = true;
            return resultado;
        } else{
            return undefined;
        }
    }
};

let fn = (a,b,c) => (a + b + c);
let onceFn = once(fn);