#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

class Node {
public:
  Node(int v) {
    val = v;
    left = nullptr;
    right = nullptr;
  }

  // setting the left child
  void setLeft(Node* n) {
    left = n;
  }

  // getting the left child
  Node* getLeft() {
    return left;
  }

  // setting the right child
  void setRight(Node* n) {
    right = n;
  }

  // getting the right child
  Node* getRight() {
    return right;
  }

private:
  Node* left;
  Node* right;
  int val;
};

// getting the height of the subtree
int getHeight(Node* node) {
  if (!node) return 0;
  return max(getHeight(node->getLeft()),
             getHeight(node->getRight()))+1;
}

// is it balanced tree?
bool isBalanced(Node* node) {
  if (!node) return true;
  int left_height = getHeight(node->getLeft()); // get the left subtree's height
  int right_height = getHeight(node->getRight()); // get the right subtree's height

  if (abs(left_height - right_height) >= 2) {
    return false;
  }

  // recursion for the subtrees
  return isBalanced(node->getLeft()) && isBalanced(node->getRight());
}
