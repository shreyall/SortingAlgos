import random

arr = []

for i in range(0, 5):
    n = random.randint(1, 30)
    arr.append(n)

print("arr now: ", arr)


# swaps two elements
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


# implements selection sort algo
def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if(arr[j] < arr[min]):
                min = j
        swap(arr, min, i)

    return arr


print(selectionSort(arr))
