# python3 mergeSort.py
import sys

def merge(arr, start, splitIndex, lastIndex):
    leftSize = splitIndex - start + 1
    rightSize = lastIndex - splitIndex
    
    leftHalf = []
    rightHalf = []
    for i in range(leftSize):
        leftHalf.append(arr[start + i])
    for i in range(rightSize):
        rightHalf.append(arr[splitIndex + i + 1])
    
    leftHalf.append(sys.maxsize)
    rightHalf.append(sys.maxsize)

    leftIndex = 0
    rightIndex = 0
    for keyIndex in range(start, lastIndex + 1):
        if leftHalf[leftIndex] <= rightHalf[rightIndex]:
            arr[keyIndex] = leftHalf[leftIndex]
            leftIndex += 1
        else:
            arr[keyIndex] = rightHalf[rightIndex]
            rightIndex += 1


def mergeSort(arr, start, lastIndex):
    if (start < lastIndex):
        splitIndex = (start + lastIndex) // 2 # we use // to only get whole numbers/indexes
        mergeSort(arr, start, splitIndex)
        mergeSort(arr, splitIndex + 1, lastIndex)
        merge(arr, start, splitIndex, lastIndex)


def main():
    arr = [ 8, 6, 7, 5, 3, 0, 9 ]
    expected = [ 0, 3, 5, 6, 7, 8, 9 ]
    print("Running insertion sort on following list:")
    print(*arr, sep=' ')

    lastIndex = len(arr) - 1
    
    mergeSort(arr, 0, lastIndex)
    
    print("Result sorted:")
    print(*arr, sep=' ')
    if arr == expected:
        print("Sorted correctly!")
    else:
        print("Did not sort correctly!")

if __name__ == "__main__":
    main()
