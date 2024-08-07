def numberToWords(num:int):
    d = {0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        100: "Hundred",
        1000: "Thousand",
        1000000: "Million",
        1000000000: "Billion"
        }
    numList = list(str(num))
    text = ""
    if num == 0:
        return "Zero"
    while num > 0:
        if int(numList[0]) == 0:
            numList.pop(0)
        elif num >= 1000000000:
            num -= (int(numList[0]) * 1000000000)
            text += f"{d[int(numList[0])]} Billion "
            numList.pop(0)
        elif num >= 100000000:
            num -= (int(numList[0]) * 100000000)
            text += f"{d[int(numList[0])]} Hundred "
            if int(numList[1]) == 0 and int(numList[2]) == 0:
                text += f"Million "
            numList.pop(0)
        elif num >= 10000000:
            if int(numList[0]) == 1:
                num -= (int(numList[0] + numList[1]) * 1000000)
                text += f"{d[int(numList[0] + numList[1])]} Million "
                numList.pop(0)
                numList.pop(0)
            else:
                num -= (int(numList[0]) * 10000000)
                text += f"{d[int(numList[0]+'0')]} "
                if int(numList[1]) == 0:
                    text += f"Million "
                numList.pop(0)
        elif num >= 1000000:
            num -= (int(numList[0]) * 1000000)
            text += f"{d[int(numList[0])]} Million "
            numList.pop(0)
        elif num >= 100000:
            num -= (int(numList[0]) * 100000)
            text += f"{d[int(numList[0])]} Hundred "
            if int(numList[1]) == 0 and int(numList[2]) == 0:
                text += f"Thousand "
            numList.pop(0)
        elif num >= 10000:
            if int(numList[0]) == 1:
                num -= (int(numList[0] + numList[1]) * 1000)
                text += f"{d[int(numList[0] + numList[1])]} Thousand "
                numList.pop(0)
                numList.pop(0)
            else:
                num -= (int(numList[0]) * 10000)
                text += f"{d[int(numList[0]+'0')]} "
                if int(numList[1]) == 0:
                    text += f"Thousand "
                numList.pop(0)
        elif num >= 1000:
            num -= (int(numList[0]) * 1000)
            text += f"{d[int(numList[0])]} Thousand "
            numList.pop(0)
        elif num >= 100:
            num -= (int(numList[0]) * 100)
            text += f"{d[int(numList[0])]} Hundred "
            numList.pop(0)
        elif num >= 10:
            if int(numList[0]) == 1:
                num -= int(numList[0] + numList[1])
                text += f"{d[int(numList[0] + numList[1])]}"
                numList.pop(0)
                numList.pop(0)
            else:
                num -= (int(numList[0]) * 10)
                text += f"{d[int(numList[0]+'0')]} "
                numList.pop(0)
        elif num >= 0:
            num -= int(numList[0])
            text += f"{d[int(numList[0])]}"
            numList.pop(0)
    if text[-1] == " ":
        text = text.rstrip()
    return text

num = 1000000000
print(numberToWords(num))