import math
p = [3,3]
q = [1,9]
print(math.dist(p,q))
########################
def euclid(a,b):
    s = 0
    for i in range(len(a)):
        s += (a[i] - b[i]) ** 2
    return s ** 0.5

print(euclid([3,3],[1,9]))







