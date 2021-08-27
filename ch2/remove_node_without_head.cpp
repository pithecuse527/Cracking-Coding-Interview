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
  Node<T>* solve(Node<T>* node) {   // parameter node cannot be a head
    Node<T>* next_node = node->getNext();
    node->setData(next_node->getData());  // copy the next node data
    node->setNext(next_node->getNext());
    delete next_node;
  }
};

int main() {
  Node<int>* n1 = new Node<int>(1);
  Node<int>* n2 = new Node<int>(2);
  Node<int>* n3 = new Node<int>(3);
  Node<int>* n4 = new Node<int>(4);
  Node<int>* n5 = new Node<int>(5);

  n1->setNext(n2);
  n2->setNext(n3);
  n3->setNext(n4);
  n4->setNext(n5);

  Solution<int> s;
  s.solve(n3);  // remove n3 from linked list

  Node<int>* runner = n1;
  while(runner) {
    cout << runner->getData() << endl;
    runner = runner->getNext();
  }
}
