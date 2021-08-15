def recursion(n):
    if n < 2:
        return '*'
    else:
        return '*' * n + '\n' + recursion(n-1)

    
#result = recursion(20)
#print(result)

def fill(n):

    return star

def void(n):
    return  
def star_draw(n):
    original = n
    if n < 2:
        return '*' * original
    else:
        row_count = 0
        star = ''
        if n % 3 == 1 and row_count % 3 ==1:
            star += ' '
            row_count += 1
        elif n % 3 != 1 and row_count % 3 != 1:
            star += '*'
            row_count += 1
        elif row_count == original:
            return star + '\n' + star_draw(n-1)

star_draw(27)

star = '*' + '*' + ' ' + '*'
print(star)