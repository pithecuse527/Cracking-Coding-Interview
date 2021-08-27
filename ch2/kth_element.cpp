#include <iostream>

using namespace std;

template<class T>
class Node {
private:
  T data;
  Node* next;
public:
  Node(T d) {
    data = d;
  }
  bool setNext(Node* node) {
    next = node;
  }
  Node* getNext() {
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
  Node<T>* solve(Node<T>* node, int k) {
    static int i = 0;   // shared by every recursive call
    if (node == NULL) return NULL;

    Node<T> to_return = solve(node->getNext(), k);  // going down with recursive call
    i++;  // going up to the start
    if (i == k) { // found kth element (the k is from the end of the linked list)
      return node;
    }
    return to_return;
  }

};
