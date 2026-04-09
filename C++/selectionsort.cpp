#include <iostream>

void selection(int A[], int n){
    for(int i = 0; i < n; i++){
        int buff = i;
        for(int j = 0; j < n - i; j++){
            if(A[i+j] < A[buff]){
                buff = i+j;
            }
        }
        std::swap(A[buff], A[i]);
    }
}

int main(){
    int L[] = {73, 12, 45, 98, 6, 34, 81, 27, 59, 99};
    int sz = sizeof(L)/sizeof(L[0]);

    selection(L, sz);

    for (int i = 0; i < sizeof(L)/sizeof(L[0]); ++i) {
        std::cout << L[i] << " ";
    }
    
    std::cin.get();
    return 0;
}