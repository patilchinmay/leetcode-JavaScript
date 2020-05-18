// https://leetcode.com/problems/subtree-of-another-tree/submissions/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} s
 * @param {TreeNode} t
 * @return {boolean}
 */

var isSubtree = function(s, t) {
    let s_arr = []
    let t_arr = []

    let temp = s
    printTree(temp, s_arr);


    let temp2 = t
    printTree(temp2, t_arr);


    s_str = s_arr.join(" ");
    t_str = t_arr.join(" ");
    // console.log(s_str);
    // console.log(t_str);

    var str = s_str
    var patt = new RegExp(t_str);

    return patt.test(str);
};

function printTree(node, arr){
    arr.push('#'+node.val);

    if (node.left){
        printTree(node.left, arr);
    }else if (node.left == undefined){
        arr.push('lnull');
    }

    if (node.right){
        printTree(node.right, arr);
    }else if (node.right == undefined){
        arr.push('rnull');
    }
}
