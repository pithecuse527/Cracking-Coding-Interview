#include <iostream>
#include <stack>

using namespace std;

stack<int> sortStack(stack<int>& stk){
  stack<int> sorted_stk;
  int to_be_pushed;

  while(!stk.empty()) {
    to_be_pushed = stk.top();
    stk.pop();
    while(!sorted_stk.empty() && sorted_stk.top() > to_be_pushed) {
      stk.push(sorted_stk.top());
      sorted_stk.top();
    }
    sorted_stk.push(to_be_pushed);
  }

  return sorted_stk;
}

int main() {
  stack<int> stk;
  for (int i=5; i>-1; i--) {
    stk.push(i);
  }
  stack<int> sorted_stk = sortStack(stk);
  for (int i=5; i>-1; i--) {
    cout << i << endl;
  }
  return 0;
}
