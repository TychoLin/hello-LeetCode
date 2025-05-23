function lengthOfLastWord(s) {
  let length = 0;
  let i = s.length - 1;

  // Skip trailing spaces
  while (i >= 0 && s[i] === " ") {
    i--;
  }

  // Count characters until we hit a space or the beginning of the string
  while (i >= 0 && s[i] !== " ") {
    length++;
    i--;
  }

  return length;
}
