// https://leetcode.com/problems/climbing-stairs/
// https://leetcode.com/submissions/detail/294136932/

/**
 * @param {number} n
 * @return {number}
 */

let cache = {};

var climbStairs = function(n) {
    if(cache[n]){
        return cache[n]
    }else{
        if(n <= 2) {
            cache[n] = n;
            return n;  
        }else{
            cache[n] = climbStairs(n-1) + climbStairs(n-2);
            return cache[n];
        }
    }
};