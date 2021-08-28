import util


def fence(n: int, f: list):
    ans = 0
    for i in range(0, len(f)):
        c = f[i]
        for j in range(i+1, len(f)):
            if f[j] >= f[i]:
                c += f[i]
            else:
                break
        for j in range(i-1, -1, -1):
            if f[j] >= f[i]:
                c += f[i]
            else:
                break
        if c > ans:
            ans = c
    return ans


def fence_de_2(l:list, left: int, right: int):
    if left == right:
        return l[left]
    mid = (left + right) // 2
    ret = max(fence_de_2(l, left, mid), fence_de_2(l, mid+1, right))
    lo = mid
    hi = mid+1
    height = min(l[lo], l[hi])
    ret = max(ret, height * 2)
    while left < lo or hi < right :
        if hi < right and (lo == left or l[lo-1] < l[hi+1]):
            hi = hi + 1
            height = min(height, l[hi])
        else:
            lo = lo -1
            height = min(height, l[lo])
        ret = max(ret, height * (hi - lo + 1))
    return ret


def executor():
    l = util.readInput("fence.txt")
    for i in range(1, 1+(int(l[0][0])*2), 2):
        n = int(l[i][0])
        f = list(map(int, l[i+1]))
        print(fence(int(l[i][0]), f))
        print(fence_de_2(f, 0, n-1))


if __name__ == '__main__':
    executor()