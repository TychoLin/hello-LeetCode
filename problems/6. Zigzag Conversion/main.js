/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function (s, numRows) {
  if (numRows === 1 || numRows >= s.length) {
    return s;
  }

  const results = Array(numRows).fill("");
  let row = 0;
  let changeDirection = false;

  for (const c of s) {
    results[row] += c;
    if (row === 0 || row === numRows - 1) {
      changeDirection = !changeDirection;
    }
    row += changeDirection ? 1 : -1;
  }

  return results.join("");
};
