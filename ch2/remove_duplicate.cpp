#include <iostream>
#include <unordered_map>

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
  void solve1(Node<T>* runner) { // with tmp buffer -- O(n)
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

  void solve2(Node<T>* pivot) {  // without any buffer -- O(n^2)
    if (pivot == NULL) return;
    Node<T>* runner = pivot;
    Node<T>* prev = runner;
    pivot = pivot->getNext();

    while (pivot) { // pivot goes through the entire linked list
      while (runner != pivot) { // scanning for the sublist
        if (runner->getData() == pivot->getData()) {
          prev->setNext(runner->getNext());
          delete runner;
          runner = prev;
        }
        runner = runner->getNext();
      }
      pivot = pivot->getNext();
    }
  }

};
