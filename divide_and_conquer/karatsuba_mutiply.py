def normalization(l: list):
    for i in range(0, len(l) - 1):
        c = l[i]
        if c >= 10:
            l[i] = c % 10
            l[i + 1] = l[i + 1] + (c // 10)
        if c < 0:
            l[i] = 10 + c
            l[i + 1] = l[i + 1] - 1

def deNormalization(l:list):
    r = 0
    for i in range(len(l)):
        r += l[i] * (10 ** i)
    return r

def multiple(a: list, b: list):
    c = [0 for _ in range(len(a) + len(b) + 1)]
    for i in range(0, len(a)):
        for j in range(0, len(b)):
            c[i + j] = c[i + j] + a[i] * b[j]
    normalization(c)
    return c


def makeIntToList(a: int):
    l = []
    while a > 0:
        l.append(a % 10)
        a = a // 10
    return l


def karatsuba_multiply(l1: list, l2: list):
    if len(l1) < 4 or len(l2) < 4:
        return multiple(l1, l2)
    l11 = l1[0: len(l1) // 2]
    l12 = l1[len(l1) // 2: len(l1)]
    l21 = l2[0: len(l2) // 2]
    l22 = l2[len(l2) // 2: len(l2)]
    r0 = karatsuba_multiply(l11, l21)
    r11 = karatsuba_multiply(l12, l21)
    r12 = karatsuba_multiply(l11, l22)
    r2 = karatsuba_multiply(l12, l22)
    r = [0 for _ in range(len(r2) + len(l1) // 2 + len(l2) // 2)]
    for i in range(0, len(r) - 1):
        if i < len(r0):
            r[i] += r0[i]
        if (len(l1) // 2) <= i < (len(l1) // 2 + len(r11)):
            r[i] += r11[i - len(l1) // 2]
        if (len(l2) // 2) <= i < (len(l2) // 2 + len(r12)):
            r[i] += r12[i - len(l2) // 2]
        if i >= len(l1) // 2 + len(l2) // 2:
            r[i] += r2[i - (len(l1) // 2 + len(l2) // 2)]
    normalization(r)
    return r


def add(l1: list, l2: list):
    r = [0 for _ in range(len(l1) + 1 if len(l1) > len(l2) else len(l2) + 1)]
    for i in range(0, len(r)):
        if i < len(l1):
            r[i] += l1[i]
        if i < len(l2):
            r[i] += l2[i]
    normalization(r)
    return r


def minus(l1: list, l2: list):
    r = [0 for _ in range(len(l1))]
    for i in range(0, len(r)):
        r[i] += l1[i]
        if i < len(l2):
            r[i] -= l2[i]
    normalization(r)
    return r


def karatsuba_multiply2(l1: list, l2: list):
    if len(l1) < 4 or len(l2) < 4:
        return multiple(l1, l2)
    d = 0
    if len(l1) > len(l2):
        d = len(l2) // 2
    else:
        d = len(l1) // 2

    l11 = l1[0: d]
    l12 = l1[d: len(l1)]
    l21 = l2[0: d]
    l22 = l2[d: len(l2)]
    r0 = karatsuba_multiply2(l11, l21)
    normalization(r0)
    r2 = karatsuba_multiply2(l12, l22)
    normalization(r2)
    r1 = minus(karatsuba_multiply2(add(l11, l12), add(l21, l22)), add(r0, r2))
    normalization(r1)

    r = [0 for _ in range(len(r2) + (d * 2))]
    for i in range(0, len(r) - 1):
        if i < len(r0):
            r[i] += r0[i]
        if d <= i < d + len(r1):
            r[i] += r1[i - d]
        if d*2 <= i:
            r[i] += r2[i - d*2]
    normalization(r)
    return r


# 28782
if __name__ == '__main__':
    l1 = makeIntToList(4234234234)
    l2 = makeIntToList(2342342342342)
    print(l1, l2)
    result = multiple(l1, l2)
    result2 = karatsuba_multiply(l1, l2)
    result3 = karatsuba_multiply2(l1, l2)

    print(result)
    print(result2)
    print(result3)
    print(deNormalization(result3))