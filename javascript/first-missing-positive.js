// https://leetcode.com/problems/first-missing-positive/
// https://leetcode.com/submissions/detail/272154910/

/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    nums = nums.sort((a,b)=>a-b);

    nums = [...new Set(nums)];

    while(nums[0] <= 0){
        nums.shift();
    }

    // console.log(nums);

    let expected = 1;

    for(let i = 1; i < nums.length; i++){
        if(nums[i] == nums[i-1] + 1){

        }else{
            expected = nums[i-1] + 1;
            break;
        }
    }

    // console.log(expected);

    if(expected != 1){
        if(nums[0] == 1){
            return expected;
        }else{
            return 1;
        }
    }else{
        if(nums[0] == 1){
            return nums[nums.length-1]+1;
        }else{
            return 1;
        }
    }
};
