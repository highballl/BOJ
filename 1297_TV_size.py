import math

d, h, w = map(int, input().split())
deg = math.sqrt((d*d) / (h*h + w*w))
print(math.floor(h*deg), math.floor(w*deg)) 