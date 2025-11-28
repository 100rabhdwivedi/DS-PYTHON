#Count how many times a perticular number appairs
list = [1,1,1,2,2,2,3,3,3,4,4,4]

dic = {}

for item in list:
    if(dic.get(item)):
        dic[item] = dic.get(item) +1
    else:
        dic[item] = 1 

print(dic)