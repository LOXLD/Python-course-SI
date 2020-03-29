from numpy import *
from timeit import default_timer as timer

dane=[[9,1,1,1,0,0,0,8,10,11,14,2132323,24234524], 2]
numbers = []
indexes = []

while len(indexes) < 3:
    for i in range (len(dane[0])):
        if len(indexes) == 3:
            break
        if dane[0][i] > dane[1]:
            numbers.append(dane[0][i])
            indexes.append(i)
        else:
            i+=1

def bubblesort(data1,data2):
    new_data = data1[:]
    new_data2 = data2[:]
    start = timer()
    for i in range(len(new_data) - 1, 0, -1):
        for j in range(i):
            if new_data[j] < new_data[j + 1]:
                new_data[j], new_data[j + 1] = new_data[j + 1], new_data[j]
                new_data2[j], new_data2[j + 1] = new_data2[j + 1], new_data2[j]
    end = timer()
    print('sorting tooked: ', end - start, 's by bubble sort method')
    return new_data2

def selectionSort(data,data2):
    new_data = data[:]
    new_data2 = data2[:]
    start = timer()
    for i in range(len(new_data)):
        currentMin = i
        for j in range(i + 1, len(new_data)):
            if new_data[j] > new_data[currentMin]:
                currentMin = j
        new_data[currentMin], new_data[i] = new_data[i], new_data[currentMin]
        new_data2[currentMin], new_data2[i] = new_data2[i], new_data2[currentMin]
    end = timer()
    print('sorting tooked: ', end - start, 's by selection method')
    return new_data2


print('\n')
print(bubblesort(numbers, indexes))
print('\n')
print(selectionSort(numbers, indexes))

