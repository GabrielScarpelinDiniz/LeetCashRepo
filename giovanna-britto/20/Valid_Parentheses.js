/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let pilha = [];
    let abertoFechado = {
        ")": "(",
        "]": "[",
        "}": "{"
    };

    for (let i = 0; i < s.length; i++){
        if ((s[i] === "(") || (s[i] === "[") || (s[i] === "{")){
            pilha.push(s[i]);
        } else {
            if (pilha.pop() !== abertoFechado[s[i]]){
                return false;
            }
        }
    }

    return (pilha.length == 0);
};