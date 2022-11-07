function maximum69Number (num: number): number {
    let numString:string = num.toString()
    let convert:boolean = true
    let output:string = ""
    for (let i:number = 0; i < numString.length; i++){
        if (numString[i] == '6' && convert){
            output += '9'
            convert = false
        }
        else output += numString[i]
    }
    return Number(output)
};

const num1323:number = 9999
console.log(maximum69Number(num1323))