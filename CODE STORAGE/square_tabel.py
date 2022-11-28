
for i in range(0, 100, 10):
    for t in range(i, i + 10):
        print(f'{t:2d}**2 = {t ** 2:<4d}', end='| ')
    print()
    a = [int(i) for i in input().split()]
    for t in range(i, i + 10):
        print(f'{t:2d}**2 = {a[t - i]:<4d}', end='| ')
    print()

