/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if (strs.length == 0){
        return ""
    } 

    prefixo = strs[0];

    for (let i = 1; i < strs.length; i++){
        while (!strs[i].startsWith(prefixo)){
            prefixo = prefixo.slice(0, -1);
            if (prefixo === ""){
                return "";
            }
        }
    }

    return prefixo;
};