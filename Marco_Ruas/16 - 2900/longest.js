/**
 * @param {string[]} words
 * @param {number[]} groups
 * @return {string[]}
 */
var getLongestSubsequence = function(words, groups) {

     const result = [];
    if (words.length === 0) return result;

    result.push(words[0]); 
    let lastGroup = groups[0];

    for (let i = 1; i < words.length; i++) {
        if (groups[i] !== lastGroup) {
            result.push(words[i]);
            lastGroup = groups[i];
        }
    }

    return result;
    
};