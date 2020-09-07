import time


def insertion_sort(data, visualizedData, timeTick):
    for i in range(1, len(data)):

        key = data[i]

        j = i-1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        visualizedData(data, ['green' if x == j+1 or x ==
                        i else 'red' for x in range(len(data))])
        time.sleep(timeTick)
    visualizedData(data, ['green' for x in range(len(data))])
