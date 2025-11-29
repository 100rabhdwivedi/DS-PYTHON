#Count how many times a perticular number appairs
list = [1,1,1,2,2,2,3,3,3,4,4,4]

dic = {}

for item in list:
    if(dic.get(item)):
        dic[item] = dic.get(item) +1
    else:
        dic[item] = 1 

print(dic)

#Soluition 2 

list1 = [1,1,1,2,2,2,3,3,3,4,4,4,41,1,4,2,3,5,6,7,8,9]

dic1 = {}

for item in list1:
    if (item in dic1.keys()):
        dic1[item] +=1
    else:
        dic1[item] = 1    
print(dic1)     

#leet code problen 771

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
       dic = {}

       for i in stones:
            if i in dic.keys():
                dic[i] = dic.get(i)+1
            else:
                dic[i] = 1
       count = 0
       for i in jewels:
            if i in dic:
                count+=dic[i] 
       return count  

#leetcode problem 1832

class Solution(object):
    def checkIfPangram(self, sentence):
        dec = {

        }
        
        for i in sentence:
            if i in dec.keys():
                dec[i]+=1
            else:
                dec[i] = 1
        if len(dec.keys())==26:
            return True
        else :
            return False  

#leetcode problem 2351

class Solution(object):
    def repeatedCharacter(self, s):
        dec = {}

        for i in s:
            if(dec.get(i)==1):
                return i
            else:
                dec[i] = 1  
                               