/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function (nums) {
  let n = nums.length;
  let maxReach = 0;

  for (let i = 0; i < n; i++) {
    if (i > maxReach || maxReach >= n - 1) break;
    maxReach = Math.max(maxReach, i + nums[i]);
  }

  return maxReach >= n - 1;
};
