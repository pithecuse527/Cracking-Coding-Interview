#include <iostream>
#include <stack>

using namespace std;

class MyQueue {
private:
  stack<int> stk1;  // save every stk2 element to the stk1 oppsite direction
  stack<int> stk2;  // enqueue here first

public:
  void stackShift() {
    if (stk1.empty()) { // lazy approach (shift when stk1 is empty only)
      while(!stk2.empty()) {
        stk1.push(stk2.top());
        stk2.pop();
      }
    }
  }

  void enqueue(int val) {
    stk2.push(val);
  }

  int dequeue() {
    stackShift();
    int to_return = stk1.top();
    stk1.pop();

    return to_return;
  }
};
