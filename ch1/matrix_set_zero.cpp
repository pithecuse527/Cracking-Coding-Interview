#include <iostream>

using namespace std;

class Solution {
public:
  void solve(int* matrix, int rows, int cols) {
    static bool row_zero_loc[rows];  // static array will be initialized to 0
    static bool col_zero_loc[cols];

    // find the index which has 0
    for (int i=0; i<rows; i++) {
      for (int j=0; j<cols; j++) {
        if (matrix[i][j] == 0) {
          row_zero_loc[i] = true;
          col_zero_loc[j] = true;
        }
      }
    }

    // matrix[i][j] should be 0 with row_zero_loc and col_zero_loc
    for (int i=0; i<rows; i++) {
      for (int j=0; j<cols; j++) {
        if (row_zero_loc[i] || col_zero_loc[j]) {
          matrix[i][j] = 0;
        }
      }
    }
  }

};
