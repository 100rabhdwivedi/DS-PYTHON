#1.Number with exactly 3 factors

n = int(input())

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

for i in range(1, n+1):
    root = int(i**0.5)
    
    
    if root * root == i:
        
        if is_prime(root):
            print(i, end=" ")

#2. Armstrong number 

# write your code here 

n = int(input())

temp = n
sum = 0
while temp> 0 :
    ldigit = temp % 10
    sum+=(ldigit**3)
    temp //=10

if (sum == n):
    print("Armstrong")
else:
    print("Not Armstrong") 

#3.Print factors of a number 

# write your code here

n = int(input())

if n == 1:
    print(1)
    exit()

print(1,end=" ")
for i in range(2,(n//2)+1):
    if n % i == 0:
        print(i,end=" ")
print(n,end=" ")     

# 4. Anargams 

# write your code here
str1 = input()
str2 = input()

count = 0
if len(str1) != len(str2):
    print("Not Anagram")
    exit()

for i in  range(len(str1)):
    if str1[i] in str2 and str2[i] in str1  :
        count+=1
        
if count == len(str1)  :
    print("Anagram")
else:
    print("Not Anagram")

#5. print perfect square
a,b = map(int,input().split())

for i in range(a,b+1):
    if i == int(i**0.5)*int(i**0.5):
        print(i,end=" ")    
