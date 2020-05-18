// https://leetcode.com/problems/rotting-oranges/
// https://leetcode.com/submissions/detail/331917062/
/**
 * @param {number[][]} grid
 * @return {number}
 **/
var orangesRotting = function(grid) {
    const rows = grid.length;
    const cols = grid[0].length;
    const dirs = [[1, 0], [0, 1], [0, -1], [-1, 0]];
    const queue = [];

    var minutes = 0;
    let population = rows * cols;
    let freshOrangeCount = 0;

    // Find all rotten oranges....
    grid.forEach((row, r) => {
        row.forEach((orange, c) => {
          if (orange === 2) {
            queue.push([r, c]);
          }else if (orange ===  1){
              freshOrangeCount++
          }
        });
    });

    // no fresh oranges at minute 0
    if(freshOrangeCount==0) return 0;

    while (queue.length) {

        // console.log(`minutes = ${minutes} : queue = ${queue.toString()}`)

        for (let i = queue.length; i > 0; --i) {
            const rottenOrange = queue.shift();

            // Loop through all possible directions
            dirs.forEach(dir => {
                const target = [rottenOrange[0] + dir[0], rottenOrange[1] + dir[1]];

                    // If orange exists in grid and orange is fresh
                    // rot it
                    if (
                          target[0] >= 0 &&
                          target[0] < rows &&
                          target[1] >= 0 &&
                          target[1] < cols &&
                          grid[target[0]][target[1]] === 1
                    ) {
                      queue.push(target);
                      // Rot Orange
                      grid[target[0]][target[1]] = 2;
                    }
                });
            }
        minutes++;
        }

    let freshOrangeExists = false;
    // check if any fresh orange is there
    for(let i=0; i<rows; i++){
        for(let j=0; j<cols; j++){
            if (grid[i][j] === 1) {
                console.log(`Fresh Orange Found at last`)
                freshOrangeExists = true;
                break;
            }
        }
    }

    return freshOrangeExists ? -1 : minutes-1;
}
