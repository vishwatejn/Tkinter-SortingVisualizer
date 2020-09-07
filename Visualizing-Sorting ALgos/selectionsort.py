import time


def selection_sort(data, visualizedData, timeTick):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        visualizedData(data, ['green' if x < i+1 or x ==
                        min_idx else 'red' for x in range(len(data))])
        time.sleep(timeTick)
    visualizedData(data, ['green' for x in range(len(data))])
