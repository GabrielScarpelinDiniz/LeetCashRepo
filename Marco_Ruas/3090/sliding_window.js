/**
 * @param {string} s
 * @return {number}
 */
var maximumLengthSubstring = function(s) {
    let l = 0;
    let r = 0;
    let max = 0;
    let dict = new Map();

    while (r < s.length) {
        dict.set(s[r], (dict.get(s[r]) || 0) + 1);

        while (dict.get(s[r]) > 2) {
            dict.set(s[l], dict.get(s[l]) - 1);
            if (dict.get(s[l]) === 0) {
                dict.delete(s[l]);
            }
            l++;
        }

        max = Math.max(max, r - l + 1);
        r++;
    }

    return max;
};