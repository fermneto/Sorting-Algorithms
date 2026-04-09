#include <iostream>

void insertion(int A[], int n){
    for(int i = 1; i < n; i++){
        int buff = A[i];
        for(int j = 0; j < i; j++){
            if(A[i-j-1] > buff){
                std::swap(A[i-j-1], A[i-j]);
            }
            else {break;}
        }
    }
}

int main(){
    int L[] = {73, 12, 45, 98, 6, 34, 81, 27, 59, 90};
    int sz = sizeof(L)/sizeof(L[0]);

    insertion(L, sz);

    for (int i = 0; i < sizeof(L)/sizeof(L[0]); ++i) {
        std::cout << L[i] << " ";
    }
    
    std::cin.get();
    return 0;
}