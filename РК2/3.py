m = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

for i in m:
    print(" ".join("{:>2}".format(s) for s in i))

size = len(m)
for layer in range(size // 2):
    if layer % 2 != 0:
        first = layer
        last = size - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = m[first][i]
            m[first][i] = m[last - offset][first]
            m[last-offset][first] = m[last][last - offset]
            m[last][last - offset] = m[i][last]
            m[i][last] = top

print()
for i in m:
    print(" ".join("{:>2}".format(s) for s in i))    


max_count = 0
index_of_max_count = -1
for j in range(size):
    col_sum = 0
    for i in range(size):
        col_sum += m[i][j]
    count = 0
    for k in range(j+1, size):
        sum_to_compare = 0
        for s in range(size):
            sum_to_compare += m[s][k]
            if sum_to_compare == col_sum:
                count += 1
        if count > max_count:
            index_of_max_count = j

print()
for i in m:
    print(" ".join("{:>2}".format(s) for s in i))

for i in range(len(m)):
    for j in range(i+1):
        m[i][j], m[j][i] = m[j][i], m[i][j]

print()
for i in m:
    print(" ".join("{:>2}".format(s) for s in i))
