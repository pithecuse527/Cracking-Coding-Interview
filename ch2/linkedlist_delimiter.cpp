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
  Node<T>* solve(Node<T>* node, T delimiter) {
    Node<T>* before_node_runner = nullptr;
    Node<T>* after_node_runner = nullptr;
    Node<T>* after_start;
    Node<T>* node_next;

    while(node) {
      node_next = node->getNext(); // save the next location first
      // cout << node -> getData() << endl;

      // the node will be attached from the back of the before_start linked list
      if (node->getData() < delimiter) {
        node->setNext(before_node_runner);
        before_node_runner = node;
      }
      // the node will be attached from the front of the after_start linked list
      else {
        if(!after_node_runner) {  // first attachment?
          after_node_runner = node;
          after_start = node;
        }
        else {
          after_node_runner->setNext(node);
          after_node_runner = node;
        }
      }
      node = node_next;
    }

    after_node_runner->setNext(before_node_runner);
    return after_start;

  }
};

int main() {
  Node<int>* n1 = new Node<int>(1);
  Node<int>* n2 = new Node<int>(3);
  Node<int>* n3 = new Node<int>(2);
  Node<int>* n4 = new Node<int>(7);
  Node<int>* n5 = new Node<int>(5);

  n1->setNext(n2);
  n2->setNext(n3);
  n3->setNext(n4);
  n4->setNext(n5);

  Solution<int> s;
  Node<int>* runner;

  runner = s.solve(n1, 3);
  while(runner) {
    cout << runner->getData() << endl;
    runner = runner->getNext();
  }
}
