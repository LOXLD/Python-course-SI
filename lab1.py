from random import randint


def data(start,stop,size):
    lista = []
    for i in range(int(size)):
        nl = randint(start, stop)
        lista.append(nl)
    return lista


def bubblesort(data):
    nd = data[:]
    for i in range(len(nd) - 1, 0, -1):
        for j in range(i):
            if nd[j] > nd[j + 1]:
                nd[j], nd[j + 1] = nd[j + 1], nd[j]
    return nd


def selectionSort(data):
    nd = data[:]
    for i in range(len(nd)):
        currentMin = i
        for j in range(i + 1, len(nd)):
            if nd[j] < nd[currentMin]:
                currentMin = j
        nd[currentMin], nd[i] = nd[i], nd[currentMin]
    return nd


a = data(10, 100, 10)
sorted_numbers_a = bubblesort(a)
print(a, 'data from a')
print(sorted_numbers_a, 'sorted a')
print('\n')
b = data(10,100,10)
sorted_numbers_b = selectionSort(b)
print(b,'data from b')
print(sorted_numbers_b,'sorted b')
