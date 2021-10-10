#include <iostream>
#include <vector>
#include <stack>
#include <ctime>
#include <cstdlib>

using namespace std;

// partition function for every quick sort
void partition(vector<int>& arr, int low, int high, int& pvt) {
    swap(arr[pvt], arr[low]);
    int j = low;
    for (int i=low+1; i<=high; i++) {
        if (arr[i] < arr[low])
            swap(arr[i], arr[++j]);
    }
    pvt = j;
    swap(arr[low], arr[pvt]);
}

// using the median element of low, high and mid element as a pivot
void quick_sort1(vector<int>& arr, int low, int high) {
    if (low >= high)
        return;

    // finding median
    int mid = (low+high)/2;
    int pvt;
    if (arr[low] > arr[high]) {
        if(arr[low] < arr[mid])
            pvt = low;
        else if(arr[high] > arr[mid])
            pvt = high;
        else
            pvt = mid;
    }
    else {
        if(arr[high] < arr[mid])
            pvt = high;
        else if(arr[low] > arr[mid])
            pvt = low;
        else
            pvt = mid;
    }

    partition(arr, low, high, pvt);
    quick_sort1(arr, low, pvt-1);
    quick_sort1(arr, pvt+1, high);

}

// using the random element as a pivot
void quick_sort2(vector<int>& arr, int low, int high) {
    srand(std::time(nullptr));
    if (low >= high)
        return;

    int pvt = rand() % (high-low+1) + low;
    partition(arr, low, high, pvt);
    quick_sort2(arr, low, pvt-1);
    quick_sort2(arr, pvt+1, high);

}

// using the first element as a pivot
void quick_sort3(vector<int>& arr, int low, int high) {
    if (low >= high)
        return;

    int pvt = low;
    partition(arr, low, high, pvt);
    quick_sort3(arr, low, pvt-1);
    quick_sort3(arr, pvt+1, high);


}

int main() {
    // vector<int> test_arr = {15, 22, 13, 27, 12, 10, 20, 25};
    vector<int> test_arr = {1,3,2,6,8,3,2};

    quick_sort2(test_arr, 0, test_arr.size()-1);

    for (auto i : test_arr)
        cout << i << " ";
    cout << endl;

    return 0;
}
