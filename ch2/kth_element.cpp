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
  Node<T>* solve(Node<T>* node, int k) {  // recursive solution
    static int i = 0;   // shared by every recursive call
    if (node == NULL) return NULL;

    Node<T> to_return = solve(node->getNext(), k);  // going down with recursive call
    i++;  // going up to the start
    if (i == k) { // found kth element (the k is from the end of the linked list)
      return node;
    }
    return to_return;
  }

  Node<T>* solve2(Node<T>* node, int k) { // iterative solution
    Node<T>* runner1 = node;
    Node<T>* runner2 = node;

    // move runner2 for k so that runner1 and runner2 has a distance k
    for (int i=0; i<k; i++) runner2 = runner2->getNext();

    while(runner2 && runner2->getNext()) { // until runner2 reaches to the end
      runner1 = runner1->getNext(); // hop together
      runner2 = runner2->getNext();
    }

    return runner1;
  }

};
