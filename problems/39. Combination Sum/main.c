void helper(int *candidates, int candidatesSize, int target, int start,
            int *combination, int combinationSize, int **results,
            int *returnSize, int **returnColumnSizes) {
  if (target == 0) {
    results[*returnSize] = (int *)malloc(sizeof(int) * combinationSize);
    (*returnColumnSizes)[*returnSize] = combinationSize;
    for (int i = 0; i < combinationSize; i++) {
      results[*returnSize][i] = combination[i];
    }
    (*returnSize)++;
    return;
  } else if (target < 0) {
    return;
  }

  for (int i = start; i < candidatesSize; i++) {
    combination[combinationSize] = candidates[i];
    helper(candidates, candidatesSize, target - candidates[i], i, combination,
           combinationSize + 1, results, returnSize, returnColumnSizes);
  }
}

int **combinationSum(int *candidates, int candidatesSize, int target,
                     int *returnSize, int **returnColumnSizes) {
  int **results = (int **)malloc(sizeof(int *) * 150);
  *returnColumnSizes = (int *)malloc(sizeof(int) * 150);
  int *combination = (int *)malloc(sizeof(int) * target);
  *returnSize = 0;

  helper(candidates, candidatesSize, target, 0, combination, 0, results,
         returnSize, returnColumnSizes);

  free(combination);
  return results;
}
