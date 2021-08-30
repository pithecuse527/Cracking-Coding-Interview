#include <iostream>
#include <vector>

using namespace std;

template<class T>
class Node {
private:
  T data;
  Node<T>* next;
public:
  Node<T>(T d) {
    data = d;
    next = nullptr;
  }
  bool setNext(Node<T>* node) {
    next = node;
  }
  Node<T>* getNext() {
    return next;
  }
  bool setData(T d) {
    data = d;
  }
  T getData() {
    return data;
  }
};

template<class T>
class Solution {
public:
  bool solve(Node<T>* head) {
    Node<int>* slow_runner = head;
    Node<int>* fast_runner = head;
    vector<int> stk;

    while(fast_runner != nullptr && fast_runner->getNext()) {
      stk.push_back(slow_runner->getData());
      slow_runner = slow_runner->getNext();
      fast_runner = fast_runner->getNext()->getNext();
    }

    if (fast_runner != nullptr) // pass the middle one when #list is odd
      slow_runner = slow_runner->getNext();

    while (slow_runner) { // compare with the stack
      if (stk.back() != slow_runner->getData()) return false;
      slow_runner = slow_runner->getNext();
      stk.pop_back();
    }

    return true;
  }

};

int main() {
  Node<int> n1(1);
  Node<int> n2(2);
  Node<int> n3(3);
  Node<int> n4(3);
  Node<int> n5(1);
  Node<int> n6(1);

  Solution<int> s;

  n1.setNext(&n2);
  n2.setNext(&n3);
  n3.setNext(&n4);
  n4.setNext(&n5);
  n5.setNext(&n6);
  n6.setNext(nullptr);

  cout << s.solve(&n1) << endl;

  return 0;
}
