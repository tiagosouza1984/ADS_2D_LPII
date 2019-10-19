import re
for i in range (int(input())):
    var_1 = input()
    passUpper = 0
    passNum = 0
    flag = False
    if var_1.isalnum() and len(var_1) == 10 :
        for i in var_1:
            if i.isupper():
                passUpper+=1
            if i.isnumeric():
                passNum+=1
            if var_1.count(i) <= 1:
                pass
            else:
                flag = True
        if passUpper >= 2 and passNum >=3 and flag == False:
            print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')
