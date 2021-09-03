X = int(input())
STICK = 64

b = bin(X)
count = 0
for digit in b:
    if digit == '1':
        count += 1
print(count)