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

#Print factors of a number 

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