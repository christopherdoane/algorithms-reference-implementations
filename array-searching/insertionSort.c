#include <stdio.h> // printf
#include <stdlib.h> // malloc
#include <stdbool.h> // bool

/**
 * Compile with gcc insertionSort.c -g.
 * To run: ./a.out
 * To debug: gdb ./a.out followed by 'run'. 'bt full' also helps give context.
 *  Add breakpoints in gdb by 'breakpoint funcName' etc.
 *  Type 'next' to step, following enter presses result in previous command.
 */ 

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

int * copyArray(int arr[], int length) {
    int * copied = (int *) malloc(sizeof(int) * length);
    int i; // for compat with < c99
    for (i = 0; i < length; i++) {
        copied[i] = arr[i];
    }
    return copied;
}

/**
 * In-place.
 * @return int * points to an integer array.
 */
void insertionSort(int arr[], int length) {
    int j, key;
    for (j = 1; j < length; j++) {
        key = arr[j];
        int i = j - 1;
        while (i >= 0 && arr[i] > key) {
            arr[i + 1] = arr[i];
            i = i - 1;
        }
        arr[i + 1] = key;
    }
}

/**
 * Input array is copied to avoid side-effects.
 * CLRS for some reason uses 1-based indices. Correcting to be 0-based.
 * @param int unsorted[] the array we want to sort, not modified.
 * @param int length the length of the first parameter.
 *  Note: We send in the length as in C, arrays sent in a parameters decay into
 *  a pointer to the first element in the array, and the size information is
 *  lost. IE: 'int unsorted[]' as a parameter is the same as 'int * unsorted'.
 * @return int * points to an integer array.
 */
int * insertionSortVerbose(int unsorted[], int length) {
    int * sorted = copyArray(unsorted, length);
    // Insertion-sort implementation for int array
    int j;
    for (j = 1; j < length; j++) {
        int sortingElem = sorted[j];
        // Step backwards, moving elements forward while sortingElem is smaller
        // Stop when we find the correct location for the sortingElem
        int inspectingIndex = j - 1;
        while (inspectingIndex >= 0 && sorted[inspectingIndex] > sortingElem) {
            sorted[inspectingIndex + 1] = sorted[inspectingIndex];
            inspectingIndex = inspectingIndex - 1;
        }
        // then we insert it there
        sorted[inspectingIndex + 1] = sortingElem;
    }
    return sorted;
}

int calcIntArraySize(int length) {
    // Important to remember that most things are pointers
    // and one needs to take into account the actual element size stored in the total array.
    return length / sizeof(int); 
}

void printArray(int arr[], int length) {
    int i;
    for (i = 0; i < length; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[] = { 8, 6, 7, 5, 3, 0, 9 };
    int expected[] = { 0, 3, 5, 6, 7, 8, 9 };
    int size = calcIntArraySize(sizeof(arr));
    
    printf("Initial array:\n");
    printArray(arr, size);

    insertionSort(arr, size);
    
    printf("Resulting array:\n");
    printArray(arr, size);

    printf("Verdict: ");
    if (arraysSame(expected, calcIntArraySize(sizeof(expected)), arr, calcIntArraySize(sizeof(arr)))) {
        // Iterating manually, as I read that memcpy is a bad way to check equality
        // as there can be padded bits at the end of arrays in some implementations of C.
        printf("sorted correctly.\n");
    } else {
        printf("did not sort correctly!\n");
    }
}
