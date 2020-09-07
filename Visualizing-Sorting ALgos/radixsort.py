import time


def countingSort(data, exp1, visualizedData, timeTick):
    colors = ['dodger blue', 'peach puff', 'green2', 'firebrick1',
              'yellow', 'orange', 'blue2', 'cyan3', 'lime green', 'steel blue']

    n = len(data)
    output = [0] * (n)
    count = [0] * (10)
    for i in range(0, n):
        index = (data[i]/exp1)
        count[int((index) % 10)] += 1

    c = []
    for i in range(len(count)):
        c.append(count[i])

    for i in range(1, 10):
        count[i] += count[i-1]

    i = n-1
    while i >= 0:
        index = (data[i]/exp1)
        output[count[int((index) % 10)] - 1] = data[i]
        count[int((index) % 10)] -= 1
        i -= 1
    i = 0

    for i in range(0, len(data)):
        data[i] = output[i]

    visualizedData(data, [colors[j] for j in range(len(c)) for i in range(c[j])])
    time.sleep(timeTick)


def radix_sort(data, visualizedData, timeTick):

    max1 = max(data)
    exp = 1

    while max1/exp > 0:
        countingSort(data, exp, visualizedData, timeTick)
        if all(data[i] >= data[i - 1] for i in range(1, len(data))):
            break
        exp *= 10
