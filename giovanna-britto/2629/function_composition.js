/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    if(functions.length === 0){
        return function(x) {
            return x;
        }
    }
    return functions.reduceRight(function(antFn, proxFn) {
        return function(x){
            return proxFn(antFn(x));
        };
    });
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */