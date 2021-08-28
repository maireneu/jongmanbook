def fastSum(n):
    if n == 1:
        return 1
    if n % 2 == 1:
        return fastSum(n - 1) + n
    return 2 * fastSum(n / 2) + (n / 2) * (n / 2)


if __name__ == '__main__':
    print(fastSum(10))
    print(fastSum(20))
    print(fastSum(40))
