def convertTotTitle(columnNumber):
    if columnNumber < 26:
        return chr(columnNumber + 64)
    elif columnNumber < 26*27:
        title = ""
        title += chr((columnNumber//26) + 64)
        title += chr((columnNumber%26) + 64)
        return title
    elif columnNumber < 26*27*27:
        title = ""
        title += chr((columnNumber//(26*27)) + 64)
        title += chr(((columnNumber%(26*27))//27) + 64)
        title += chr(((columnNumber%(26*27))%27) + 64)
        return title
columnNumber = 2000
print(convertTotTitle(columnNumber))