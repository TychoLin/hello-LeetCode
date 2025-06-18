typedef struct {
  int x, y;
} Point;

int uniquePaths(int m, int n) {
  Point directions[] = {{0, 1}, {1, 0}};

  int **dp = (int **)malloc(m * sizeof(int *));
  for (int i = 0; i < m; ++i) {
    dp[i] = (int *)calloc(n, sizeof(int));
  }
  dp[0][0] = 1;

  Point *queue = (Point *)malloc((m + 1) * sizeof(Point));
  int front = 0, size = 1;
  queue[front] = (Point){0, 0};

  while (size > 0) {
    Point p = queue[front];
    queue[front] = (Point){-1, -1};
    front = (front + 1) % (m + 1);
    size -= 1;

    for (int i = 0; i < 2; ++i) {
      int newX = p.x + directions[i].x;
      int newY = p.y + directions[i].y;

      if (newX >= 0 && newX < m && newY >= 0 && newY < n) {
        if (dp[newX][newY] == 0) {
          int avail = (front + size) % (m + 1);
          queue[avail] = (Point){newX, newY};
          size += 1;
        }
        dp[newX][newY] += dp[p.x][p.y];
      }
    }
  }

  int result = dp[m - 1][n - 1];

  for (int i = 0; i < m; ++i) {
    free(dp[i]);
  }
  free(dp);
  free(queue);

  return result;
}
