from tkinter import *
from tkinter import ttk
from bubbleSort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort
from selectionsort import selection_sort
from heapsort import heap_sort
from insertionsort import insertion_sort
from radixsort import radix_sort
import random

root = Tk()
root.title('Sorting Algorithm Visualizer')
root.maxsize(1200, 800)
root.config(bg='black')

# variables
selected_alg = StringVar()
data = []

# Draw function

def visualizedData(data, colorArray):

    canvas.delete("all")
    c_height = 380
    c_width = 800
    x_width = c_width / (len(data) + 1)
    offset = 10
    spacing = 8
    normalizedData = [i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        # top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        # bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))

    root.update_idletasks()
# Data generator Function


def DataGenerator():
    global data
    minVal = int(miniVal.get())
    maxiVal = int(maxVal.get())
    size = int(arrSize.get())
    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxiVal+1))
    visualizedData(data, ['red' for x in range(len(data))])
# Sorting Algorithms


def StartAlgorithm():
    global data
    if not data:
        return
    if algomen.get().split(":")[0] == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, visualizedData, frameSpeed.get())
    elif algomen.get().split(":")[0] == 'Bubble Sort':
        bubble_sort(data, visualizedData, frameSpeed.get())
    elif algomen.get().split(":")[0] == 'Merge Sort':
        merge_sort(data, visualizedData, frameSpeed.get())
    elif algomen.get().split(":")[0] == "Selection Sort":
        selection_sort(data, visualizedData, frameSpeed.get())
    elif algomen.get().split(":")[0] == 'Heap Sort':
        heap_sort(data, visualizedData, frameSpeed.get())
    elif algomen.get().split(":")[0] == 'Insertion Sort':
        insertion_sort(data, visualizedData, frameSpeed.get())
    elif algomen.get().split(":")[0] == 'Radix sort':
        radix_sort(data, visualizedData, frameSpeed.get())
    visualizedData(data, ['green' for x in range(len(data))])


# frame / base layout
UI_frame = Frame(root, width=1000, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=800, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)
# User Interface Area
# Row[0]:
Label(UI_frame, text="Algorithm: ", bg='grey').grid(
    row=0, column=0, padx=5, pady=5, sticky=W)
algomen = ttk.Combobox(UI_frame, textvariable=selected_alg, values=["Radix sort: O(b*(n+k))",'Quick Sort: O(n*log(n))', 'Merge Sort: O(n*log(n))', 'Insertion Sort: O(n^2)', 'Heap Sort: O(n*log(n))', 'Selection Sort: O(n^2)', 'Bubble Sort: O(n^2)'])
algomen.grid(row=0, column=1, padx=5, pady=5)
algomen.current(0)

frameSpeed = Scale(UI_frame, from_=0.1, to=5.0, length=200, digits=2,
                   resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]")
frameSpeed.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="Start", command=StartAlgorithm,
       bg='red').grid(row=0, column=3, padx=5, pady=5)
# Row[1]
arrSize = Scale(UI_frame, from_=3, to=40, resolution=1,
                  orient=HORIZONTAL, label="Data Size")
arrSize.grid(row=1, column=0, padx=5, pady=5)

miniVal = Scale(UI_frame, from_=0, to=10, resolution=1,
                orient=HORIZONTAL, label="Min Value")
miniVal.grid(row=1, column=1, padx=5, pady=5)

maxVal = Scale(UI_frame, from_=10, to=999, resolution=1,
               orient=HORIZONTAL, label="Max Value")
maxVal.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text="DataGenerator", command=DataGenerator,
       bg='white').grid(row=1, column=3, padx=3, pady=5)

root.mainloop()
