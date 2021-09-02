#include <stack>
#include <iostream>
#include <algorithm>

using namespace std;

// we assume that the stack size is infinite
void push(stack<pair<int, int> >& stk, int val) {
  if (stk.empty()) {
    stk.push(make_pair(val, val));
    return;
  }
  int min_ = min(stk.top().first, val);
  stk.push(make_pair(val, min_));
}

int pop(stack<pair<int, int> >& stk) {
  if (stk.empty()) {
    cout << "stk is empty" << endl;
    return -1;
  }

  int to_return = stk.top().first;
  stk.pop();
  return to_return;
}

int minVal(stack<pair<int, int> >& stk) {
  if (stk.empty()) {
    cout << "stk is empty" << endl;
    return -1;
  }

  int to_return = stk.top().second;
  return to_return;
}

int main() {
  stack<pair<int, int> > my_stk;
  push(my_stk, 7);
  push(my_stk, 3);
  push(my_stk, 5);
  push(my_stk, 2);

  // cout << pop(my_stk) << endl;
  cout << minVal(my_stk) << endl;

  return 0;
}
