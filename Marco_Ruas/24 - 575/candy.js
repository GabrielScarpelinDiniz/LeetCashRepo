/**
 * @param {number[]} candyType
 * @return {number}
 */
var distributeCandies = function(candyType) {
    let objeto = {}

    for(let i = 0; i < candyType.length; i++){
        if(!objeto[candyType[i]]){
            objeto[candyType[i]] = true
        }
        
    }

    let tipos = Object.keys(objeto).length
    let maximo = candyType.length / 2

    if(tipos < maximo){
        return tipos
    }
    else{
        return maximo
    }

};