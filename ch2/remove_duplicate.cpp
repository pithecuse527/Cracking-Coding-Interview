#include <iostream>
#include <unordered_map>

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
  void solve1(Node<T>* runner) { // with tmp buffer
    Node<T>* prev = runner;
    unordered_map<T, bool> hash_map;

    while(runner) {
      // when the hash map has the T
      if (hash_map.find(runner->getData()) != hash_map.end()) {
        prev->setNext(runner->getNext());
        delete runner;
        runner = prev;
      }
      else {  // when the hash map does not have the T
        hash_map[runner->getData()] = true;
        prev = runner;
      }
    }
    runner = runner->getNext();
  }
};
