'''
key-values pair,mutable,
you can change the values only but you can't change the key
you can store duplicate value but you can't store duplicate key
'''

dic = {1:100,2:200,3:300}

dic1 = {
    "name":"Saurabh",
    "class":"mca fy",
    "age":20,
    True:20
}

print(dic)

dic[1] = 1000

print(dic)
print(dic1,dic1[True])