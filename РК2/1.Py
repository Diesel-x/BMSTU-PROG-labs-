m1 = [1, 2, 6, 6, 10, 100,1000,1200]
m2 = [2, 5, 7, 8, 10, 12]
m3 = []

i_m1 = 0
i_m2 = 0
for i in range(len(m1) + len(m2)):
    if (len(m1) == i_m1):
        m3 += m2[i_m2:]
        break
    elif (len(m2) == i_m2):
        m3+=m1[i_m1:]
        break
    if (m1[i_m1] < m2[i_m2]):
        m3.append(m1[i_m1])
        i_m1+=1
    else:
        m3.append(m2[i_m2])
        i_m2+=1
print(m3)

i_ofmax = -1
i_ofmin = -1
m3_max = float("-inf")
m3_min = float("inf")
for i in range(len(m3)):
    if (m3[i] % 2 == 0):
        if (m3[i] > m3_max):
            m3_max = m3[i]
            i_max = i
    else:
        if (m3[i] < m3_min):
            m3_min = m3[i]
            i_min = i 

print("min: ", m3_min)
print("max: ", m3_max)

m3[i_min], m3[i_max] = m3[i_max], m3[i_min]
print(m3)




