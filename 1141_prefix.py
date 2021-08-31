import sys
from collections import deque

n = int(input()) #length
words = set([sys.stdin.readline().strip() for _ in range(n)])
words = deque(sorted(words, key=lambda x:len(x)))
#print("initial",words)

def checkword(words):
    count = 0
    result = 0
    for i in range(len(words)-1):
        #print("work1")
        #print("now elem", words[i])
        prev = words[i]
        
        for j in range(i+1, len(words)):
            #print("work2")
            next = words[j]
            #print("prev",prev,"next",next)
            for i in range(len(prev)):
                #print("work3")
                if prev != next[:len(prev)]:
                    #print("is break")
                    #count += 1
                    #print("count plus", count)
                    break
                elif prev == next[:len(prev)]:
                    #words.popleft()
                    #out = words.popleft()
                    #print("checked", out)
                    print("checked", prev)
                    count = 1
                    #print(count)
                    #return checkword(words)
        result += count
        count = 0    

    return result

#print("result:",checkword(words))
#print(len(checkword(words)))
print(len(words)-checkword(words))



#words = list(sys.stdin.readline().strip() for _ in range(n))
#words_with_len = defaultdict(int)
#len_words = deque([])
#print(words_with_len)
#for i in range(n):
#    words_with_len[i]= [words[i], len(words[i])]

#words_with_len = sorted(words_with_len, key = lambda x: x.values())
#print(words_with_len[0][1])

