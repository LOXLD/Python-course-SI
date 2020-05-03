def choinka(n):
    for i in range(n):
        if i == 0:
            print(' ' * n, '#')
        else:
            print(' ' * int(n - i), '#' * i * 2)

    for i in range(3):
        print(' ' * n, '#')

choinka(20)
