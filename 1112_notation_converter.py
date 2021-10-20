import sys

input = sys.stdin.readline()

n, m = input.split()
int_n, int_m = map(int, [n, m])

def convert(n, m):
    digits = len(n)
    int_n, int_m = map(int, [n, m])
    ans = ""

    if int_n == 0:
        return 0

    while int_n != 0:
        temp = divmod(int_n, int_m)
        share = temp[0]
        rest = temp[1]
        if rest < 0:
            share += 1
            rest += abs(int_m)

        ans += str(rest)
        int_n = share
        digits -= 1
    
    return ans[::-1]

if int_n < 0 and int_m > 0:
    print('-'+convert(n[1:], m))
else:
    print(convert(n, m))
