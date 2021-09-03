#include <vector>
#include <stack>
#include <iostream>
#define STK_MAX_SIZE 10
#define STK_SET_MAX_SIZE 5

using namespace std;

template <class T>
class SetOfStacks {
public:
  vector<stack<T> > stacks;

  stack<T>* getLastStack() {
    if (stacks.empty()) return nullptr;
    return &stacks[stacks.size()-1];
  }

  bool push(T val) {
    // get the last stack to be pushed
    stack<T>* stk = getLastStack();

    // if there is no stack in the stack stacks vector,
    // or if the new stack is needed,
    if (!stk || stk->size() == STK_MAX_SIZE) {
      if (stacks.size() == STK_SET_MAX_SIZE)  // stacks vector also has a limit
        return false;
      stk = new stack<T>;
      stk->push(val);
      stacks.push_back(*stk);
      return true;
    }

    // if there is a space in the stack
    stk->push(val);
    return true;

  }

  bool pop() {
    // get the last stack to be popped
    stack<T>* stk = getLastStack();

    if (!stk) // if there is nothing to be popped
      return false;

    // pop the element
    stk->pop();

    // if the last stack is empty, pop the last stack from stacks vector,
    // and delete the stk (was a last stack)
    if(stk->empty()) {

      // pop from stacks vector
      stacks.pop_back();

      // delete the stk
      delete stk;
      stk = nullptr;
    }
    return true;
  }

  T top() {
    // get the last stack to be topped
    stack<T>* stk = getLastStack();

    if (!stk) // if there is nothing to be topped
      return 0;

    return stk->top();
  }
};


int main() {
  SetOfStacks<int> stk_set;
  for (int i=1; i<51; i++) stk_set.push(i);
  cout << stk_set.top() << endl;
  for (int i=1; i<50; i++) stk_set.pop();
  cout << stk_set.top() << endl;

  return 0;
}
