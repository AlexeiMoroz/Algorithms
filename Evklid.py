# Алгоритм Эвклида - находит наибольший общий делитель
#

def cgd(m, n):
    while m != n:
        if m > n:
            m -= n
        else:
            n -= m
    return m

def cgd2(m, n):
    if n == 0:
        return m
    return cgd2(n, m % n)

def cgd3(m, n):
    while n != 0:
        m1 = m
        m = n
        n = m1 % n
    return m

print(cgd(21, 54))
print(cgd2(21, 54))
print(cgd3(21, 54))