def countSeniors(details):
    num = 0
    for i in details:
        if int(i[11] + i[12]) > 60:
            num += 1
    return num

details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
print(countSeniors(details))