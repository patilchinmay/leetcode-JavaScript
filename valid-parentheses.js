// https://leetcode.com/problems/valid-parentheses/
// https://leetcode.com/submissions/detail/271044431/

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    if(s === undefined || typeof s != "string") throw new Error("Invalid Input");

    s = s.split('').reverse();

    let stack = [];

    for(let i = 0; i < s.length; i++){
        stack.push(s[i]);

        if(i>0){
            if( ( stack[stack.length-1] == '(' && stack[stack.length-2] == ')' ) ||
                ( stack[stack.length-1] == '[' && stack[stack.length-2] == ']' ) ||
                ( stack[stack.length-1] == '{' && stack[stack.length-2] == '}' ) ) {
                stack.pop();
                stack.pop();
            }
        }
    }

    return stack.length == 0;
};
