import sys

N, M = map(int, input().split())
input_list = [sys.stdin.readline().strip() for _ in range(N+M)]

quiz = []
pokemon = []


for i in range(N+M):
    if i < N:
        pokemon.append(input_list[i])
    else:
        quiz.append(input_list[i])

for i in range(M):
    q = quiz[i]
    if q.isalpha():
        print(pokemon.index(quiz[i])+1)
    elif q.isdigit():
        print(pokemon[int(quiz[i])-1])

