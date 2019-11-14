# python3 insertionSort.py

def insertionSort(arr):
    length = len(arr)
    j = 1
    for j in range(1, length):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key
        j += j

def main():
    arr = [ 8, 6, 7, 5, 3, 0, 9 ]
    expected = [ 0, 3, 5, 6, 7, 8, 9 ]
    print("Running insertion sort on following list:")
    print(*arr, sep=' ')
    insertionSort(arr) # in-place side-effect nastiness
    print("Result sorted:")
    print(*arr, sep=' ')
    if arr == expected:
        print("Sorted correctly!")
    else:
        print("Did not sort correctly!")

if __name__ == "__main__":
    main()
    