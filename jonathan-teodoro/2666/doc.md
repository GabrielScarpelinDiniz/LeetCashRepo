/**
 * @param {Function} fn
 * @return {Function}
 */
 var once = function(fn) {
    let called = false;
    let result;

    return function(...args) {
        if (!called) {
            called = true;
            result = fn(...args);
            return result;
        }
        return undefined;
    }
};


/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
Essa função once envolve fn e usa uma flag called para garantir que fn seja executada apenas na primeira chamada. As chamadas seguintes retornam undefined, evitando reexecução. É útil para inicializações únicas ou lógicas que não devem ser repetidas.