function reverseVowels(s: string): string {
  const vowel: Array<string> = [
    "a",
    "A",
    "e",
    "E",
    "i",
    "I",
    "o",
    "O",
    "u",
    "U",
  ];
  var output: string = "";
  var vowelnput: Array<string> = [];
  for (let i: number = 0; i < s.length; i++) {
    if (vowel.includes(s[i])) {
      vowelnput.push(s[i]);
    }
  }

  for (let i: number = 0; i < s.length; i++) {
    if (vowel.includes(s[i])) {
      output += vowelnput.pop();
    } else {
      output += s[i];
    }
  }
  return output;
}

let s345:string = "leetcode"
console.log(reverseVowels(s345))