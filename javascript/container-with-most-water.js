// https://leetcode.com/problems/container-with-most-water/
// https://leetcode.com/submissions/detail/271019459/

/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {

    let maxWater = 0;
    let i = 0, j = height.length-1;

    while( i < j ){
        maxWater = Math.max(maxWater, Math.min(height[i], height[j]) * (j - i));

        if(height[i] < height[j]){
            i++;
        }else{
            j--;
        }
    }

    return maxWater;
};
