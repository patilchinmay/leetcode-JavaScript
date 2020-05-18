// https://leetcode.com/problems/rotate-array/
// https://leetcode.com/submissions/detail/280083328/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {

    // for(let i = 0; i < k; i++){
    //     nums.splice(0,0,nums.pop());
    // }

    let myArray = nums.splice(nums.length-k, k);

    for(let i = myArray.length-1; i >= 0; i--){
        nums.splice(0,0,myArray[i]);
    }
};
