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

            