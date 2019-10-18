// https://leetcode.com/problems/palindrome-number/submissions/
// https://leetcode.com/submissions/detail/270935335/

/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    return x == `${x}`.split('').reverse().join('');
};
