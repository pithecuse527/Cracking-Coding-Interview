#include <vector>
#include <iostream>
#include <cmath>
#define STK_SIZE 10

using namespace std;

class ThreeStk {
public:
  int buffer[STK_SIZE*3];
  int stack_headers[3] = {-1, -1, -1};

  bool push(int stk_num, int val) {
    if (stack_headers[stk_num] + 1 > STK_SIZE) return false;

    stack_headers[stk_num]++;
    buffer[topOfStack(stk_num)] = val;
  }

  bool pop(int stk_num) {
    if (stack_headers[stk_num] == -1) return false;
    buffer[topOfStack(stk_num)] = 0;
    stack_headers[stk_num]--;
    return true;
  }

  // return the top of stk_num
  int topOfStack(int stk_num) {
    return stk_num*STK_SIZE+stack_headers[stk_num]
  }

};
