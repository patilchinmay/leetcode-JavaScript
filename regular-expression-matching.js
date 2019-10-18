// https://leetcode.com/problems/regular-expression-matching/
// https://leetcode.com/submissions/detail/271014534/

/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    let pattern = new RegExp('^'+p+'$', "gm");
    return pattern.test(s);
};
