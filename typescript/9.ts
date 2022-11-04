function isPalindrome(x: number): boolean | undefined{
    if (x < 0) return false
    let temp:string = x.toString()
    let tempArray:Array<string> = []
    for (let i:number = 0; i < temp.length ; i++){
        if (i < Math.floor(temp.length / 2)){
            tempArray.push(temp[i])
        }
        else{
            if (tempArray.length == temp.length - i){
                if (temp[i] != tempArray.pop()) return false
            }
        }
    }
    return true
};

const x9:number = 12221
console.log(isPalindrome(x9))