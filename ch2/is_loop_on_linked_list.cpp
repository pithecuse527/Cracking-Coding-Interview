#include <iostream>

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
  Node<T>* solve(Node<T>* head) {
    Node<T>* slow_runner = head;  // jumps one node
    Node<T>* fast_runner = head;  // jumps two nodes

    // find the collision spot (also considering the case not having the loop)
    while(1) {
      slow_runner = slow_runner->getNext();
      fast_runner = fast_runner->getNext()->getNext();

      // found the collision spot
      if (slow_runner == fast_runner) break;

      // there is no loop
      if (fast_runner != nullptr && fast_runner->getNext()) return nullptr;
    }

    // locate the slow_runner to the head again, and both runner jumps
    // with a same speed
    slow_runner = head;
    while(slow_runner != fast_runner) {
      slow_runner = slow_runner->getNext();
      fast_runner = fast_runner->getNext();
    }

    return slow_runner;
  }

};
