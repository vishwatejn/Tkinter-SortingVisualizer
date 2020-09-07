import time


def heapify(data, i,n):
    largest = i  
    l = 2 * i + 1	 
    r = 2 * i + 2	 
    if l < n and data[largest] < data[l]:
        largest = l
    if r < n and data[largest] < data[r]:
        largest = r
    if largest != i:
        data[i], data[largest] = data[largest], data[i]  # swap
        heapify(data,largest,n)


def heap_sort(data, visualizedData, timeTick):
    n = len(data)
    for i in range(n//2 - 1, -1, -1):
        heapify(data,i,n)
    for i in range(n-1, 0, -1):
        data[i], data[0] = data[0], data[i]
        visualizedData(data, ['green' if x == 0 or x ==
                        i else 'red' for x in range(len(data))])
        time.sleep(timeTick)
        heapify(data,0,i)
    visualizedData(data, ['green' for x in range(len(data))])
