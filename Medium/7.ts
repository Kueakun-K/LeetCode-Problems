function reverse(x: number): number {
  let output: string = "";
  let inputString: string = x.toString();
  let inputArray: Array<string> = [];
  for (let i: number = 0; i < inputString.length; i++) {
    if (inputString[i] == "-") output += "-";
    else inputArray.push(inputString[i]);
  }
  for (let i:number = inputArray.length - 1; i >= 0 ; i--){
    output += inputArray[i]
  }
  if (Number(output) > (2**31) || Number(output) < ((-2)**31)) return 0
  return Number(output);
}

const x7: number = -4236469;
console.log(reverse(x7));
