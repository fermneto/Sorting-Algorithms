#include <iostream>

void bubble(int arr[], int n) {
    //Repeat n-1 passes through the list, to verity every index but the last one
    for (int i = 0; i < n - 1; ++i) {
        //Each pass compares adjacent elements
        for (int j = 0; j < n - 1; ++j) {
            //Swap neighbors if they are out of order
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
            }
        }   
    }
}

int main() {
    int x[] = {98, 73, 12, 45, 6, 34, 81, 27, 59, 90};
    int n = sizeof(x)/sizeof(x[0]);

    bubble(x, n);

    for (int i = 0; i < sizeof(x)/sizeof(x[0]); ++i) {
        std::cout << x[i] << " ";
    }

    std::cin.get();
    return 0;
}