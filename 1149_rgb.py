import sys

input = sys.stdin.readline

n = int(input())
dp = []

for i in range(n):
    r, g, b = [int(x) for x in input().split()]
    if not dp:
        dp.append((r, g, b))
    else:
        prev_r, prev_g, prev_b = dp[-1]
        curr_r = r + min(prev_g, prev_b)
        curr_g = g + min(prev_r, prev_b)
        curr_b = b + min(prev_r, prev_g)
        dp.append((curr_r, curr_g, curr_b))

print(dp)
print(min(dp[-1]))


# print(costs)

# def get_permutations(rgb, pick_cnt):
#     for i in range(pick_cnt):
#         if pick_cnt == 1:
#             yield [rgb[i]]
#         else:
#             rest_color = list(filter(lambda x: x != rgb[i], rgb))
#             if i != 0:
#                 rest_color += [rgb[i-1]]
#             # for next in get_permutations(rgb[:i] + rgb[i+1:], pick_cnt - 1):
#             print('i', i, 'rest_color', rest_color)
#             for next in get_permutations(rest_color, pick_cnt - 1):
#                 yield [rgb[i]] + next


# permutation_list = list(get_permutations([0, 1, 2], 3))
# result = []
# for permu_list in permutation_list:
#     total_cost = 0
#     for i in range(n):
#         idx = i % 3
#         # print('idx', idx, permu_list, )
#         color = permu_list[idx]
#         cost = costs[i][color]
#         print('color', permu_list[idx], 'cost', cost)
#         total_cost += costs[i][color]
#     result.append(total_cost)

# print(result)

# def get_cost(color, total_cost):
#     colors = [0, 1, 2] # R, G, B
#     filtered_color = list(filter(lambda x: x != color, colors))
#     c_1 = filtered_color[0]
#     c_2 = filtered_color[1]
        
#     result = 0
#     result += total_cost + costs[i][color]

#     return result



