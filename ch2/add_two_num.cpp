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
  Node<T>* solve(Node<T>* node1, Node<T>* node2, T carry) {
    
    // base case
    if (node1 == nullptr && node2 == nullptr && carry == 0) {
      return nullptr; // indicate the end
    }
    
    T tmp_sum = 0;
    
    if (node1 != nullptr) { // when the node1 is not null
      tmp_sum += node1->getData();
      node1 = node1->getNext();
    }
    if (node2 != nullptr) { // when the node2 is not null
      tmp_sum += node2->getData();
      node2 = node2->getNext();
    }
    
    // carry?
    tmp_sum += carry;
    carry = tmp_sum / 10;
    
    Node<T>* result = new Node<T>(tmp_sum % 10); // to return
    result -> setNext(solve(node1, node2, carry)); // recursive call
    return result;
    
  }
};

int main() {
  
  // 2231
  Node<int>* n1 = new Node<int>(1);
  Node<int>* n2 = new Node<int>(3);
  Node<int>* n3 = new Node<int>(2);
  Node<int>* n4 = new Node<int>(2);
  
  // 57
  Node<int>* n5 = new Node<int>(7);
  Node<int>* n6 = new Node<int>(5);
  
  n1->setNext(n2);
  n2->setNext(n3);
  n3->setNext(n4);
  n4->setNext(nullptr);
  
  n5->setNext(n6);
  n6->setNext(nullptr);
  

  Solution<int> s;
  
  // result
  Node<int>* result = s.solve(n1,n5,0);
 
  
  while(result) {
    cout << result->getData() << endl;
    result = result->getNext();
  }
}
