bool isValid(char *s) {
  const char *lefty = "([{";
  const char *righty = ")]}";
  char *stack = malloc(strlen(s));
  int top = -1;
  int valid = 1;

  for (int i = 0; s[i] != '\0'; i++) {
    char c = s[i];

    if (c == '(' || c == '[' || c == '{')
      stack[++top] = c;
    else if (c == ')' || c == ']' || c == '}') {
      if (top == -1) {
        valid = 0;
        break;
      }
      char *p1 = strchr(lefty, stack[top--]);
      char *p2 = strchr(righty, c);
      if ((p1 - lefty) != (p2 - righty)) {
        valid = 0;
        break;
      }
    }
  }

  return (valid == 0) ? valid : top == -1;
}
