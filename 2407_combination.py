
n, m = map(int, input().split())
comb = 1
frag = 1
for i in range(m):
    comb *= (n - i)
    frag *= (i+1)

print(comb//frag)


# import itertools
# n, m = map(int, input().split())
# sets = [i+1 for i in range(n)]
# print(sets)
# result = itertools.combinations(sets,m)

# print(list(result))

