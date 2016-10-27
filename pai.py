def main():
    c = 2800
    f = [10000 / 5] * 2801
    f[c] = 0
    e = 0
    while c != 0:
        d = 0
        b = c
        while True:
            d += f[b] * 10000
            f[b] = d % (b * 2 - 1)
            d /= (b * 2 - 1)
            b -= 1
            if b == 0:
                break
            d *= b

        c -= 14
        print '%04d' % (e + d / 10000),
        e = d % 10000

    print

main()

