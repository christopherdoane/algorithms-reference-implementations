#include <stdio.h>
#include <stdbool.h>
#include <limits.h>

bool arraysSame(int first[], int sizeFirst, int second[], int sizeSecond) {
    if (sizeFirst != sizeSecond) {
        return false;
    }
    int i; // for compat with < c99
    for (i = 0; i < sizeFirst; i++) {
        if (first[i] != second[i]) {
            return false;
        }
    }
    return true;
}

int calcIntArraySize(int size) {
    return size / sizeof(int);
}

void printArray(int arr[], int length) {
    int i;
    for (i = 0; i < length; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void mergeAuxiliary(int * arr, int start, int splitIndex, int lastIndex) {
    int sizeLeft = splitIndex - start + 1;
    int sizeRight = lastIndex - splitIndex;
    int leftHalf[sizeLeft + 1]; // we add another slot to place an INFINITY elem (INT_MAX)
    int rightHalf[sizeRight + 1]; // same here, so we skip an if-case later to check for empty arrays
    int leftIndex, rightIndex;
    for (leftIndex = 0; leftIndex < sizeLeft; leftIndex++) {
        leftHalf[leftIndex] = arr[start + leftIndex];
    }
    for (rightIndex = 0; rightIndex < sizeRight; rightIndex++) {
        rightHalf[rightIndex] = arr[splitIndex + rightIndex + 1];
    }
    leftHalf[sizeLeft] = INT_MAX; // technically a bad strategy, but OK for edu purposes
    rightHalf[sizeRight] = INT_MAX;
    
    leftIndex = 0;
    rightIndex = 0;
    int keyIndex;
    for (keyIndex = start; keyIndex <= lastIndex; keyIndex++) { // since we only go to length, we will never add an infinity elem (yes ofc assuming an INT_MAX isnt part of the data set)
        if (leftHalf[leftIndex] <= rightHalf[rightIndex]) {
            arr[keyIndex] = leftHalf[leftIndex];
            leftIndex++;
        } else {
            arr[keyIndex] = rightHalf[rightIndex];
            rightIndex++;
        }
    }
}

void mergeSort(int * arr, int start, int lastIndex) {
    if (start < lastIndex) {
        int splitIndex = (start + lastIndex) / 2; // not supporting 0 sizes
        mergeSort(arr, start, splitIndex);
        mergeSort(arr, splitIndex + 1, lastIndex);
        mergeAuxiliary(arr, start, splitIndex, lastIndex);
    }
}

int main() {
    int arr[] = { 8, 6, 7, 5, 3, 0, 9 };
    int expected[] = { 0, 3, 5, 6, 7, 8, 9 };
    int size = calcIntArraySize(sizeof(arr));

    printf("Initial array:\n");
    printArray(arr, size);

    int lastIndex = size - 1;
    mergeSort(arr, 0, lastIndex);
    
    printf("Resulting array:\n");
    printArray(arr, size);

    printf("Verdict: ");
    if (arraysSame(expected, calcIntArraySize(sizeof(expected)), arr, calcIntArraySize(sizeof(arr)))) {
        printf("sorted correctly.\n");
    } else {
        printf("did not sort correctly!\n");
    }
}