import random


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        while(j > 0 & arr[j] < arr[j-1]):
            swap(arr, j, j-1)
            j = j-1

    return arr


arr = []
for i in range(0, 5):
    n = random.randint(1, 30)
    arr.append(n)

print("arr now: ", arr)
print(insertionSort(arr))
