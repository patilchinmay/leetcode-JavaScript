// https://leetcode.com/problems/two-sum/
// https://leetcode.com/submissions/detail/269785484/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    if(nums instanceof Array && typeof target == "number"){
        for(let i = 0; i < nums.length; i++){
            for(let j = 0; j < nums.length; j++){
                if(i != j){
                    if(nums[i] + nums[j] == target){
                        let answer = [];
                        answer.push(i<j?i:j);
                        answer.push(i<j?j:i);
                        return answer;
                    }
                }
            }
        }
    }else{
        throw new Error("Invalid input");
    }
};
