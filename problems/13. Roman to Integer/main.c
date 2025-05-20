int romans(char k) {
  int v = -1;

  switch (k) {
  case 'I':
    v = 1;
    break;
  case 'V':
    v = 5;
    break;
  case 'X':
    v = 10;
    break;
  case 'L':
    v = 50;
    break;
  case 'C':
    v = 100;
    break;
  case 'D':
    v = 500;
    break;
  case 'M':
    v = 1000;
    break;
  default:
    break;
  }

  return v;
}

int romanToInt(char *s) {
  int total = 0;
  int fast = 1;
  int slow = fast - 1;

  int s_l = strlen(s);

  while (fast < s_l) {
    slow = fast - 1;
    if (romans(s[fast]) <= romans(s[slow]))
      total += romans(s[slow]);
    else
      total -= romans(s[slow]);
    fast += 1;
  }
  total += romans(s[s_l - 1]);

  return total;
}
