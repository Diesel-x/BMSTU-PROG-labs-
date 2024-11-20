m = [[1,2,3,4],[1,2,3,4],[10,11,12,13],[14,15,16,17]]

def matrix_print(matrix):
    for i in matrix:
        print(" ".join("{:>3}".format(s) for s in i))

matrix_print(m)

size = len(m)
for layer in range(size // 2):
    first = layer
    last = size - 1 - layer
    for i in range(first, last):
        offset = i - first
        top = m[first][i]
        m[first][i] = m[last - offset][first]
        m[last - offset][first] = m[last][last - offset]
        m[last][last - offset] = m[i][last]
        m[i][last] = top

print()
matrix_print(m)

sums = []
for j in range(size):
    sum = 0
    for i in range(size):
        sum += m[i][j]
    sums.append(sum)

print()
print(sums)
