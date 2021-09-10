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

// getting the height of the subtree, stop searching when it founds not balanced
// worse case -- O(nlogn)
// average -- O(n)
int getHeight(Node* node) {
  if (!node) return 0;
  int left_height = getHeight(node->getLeft());
  if (left_height == -1) return -1;
  int right_height = getHeight(node->getRight());
  if (right_height == -1) return -1;

  if (abs(left_height - right_height) >= 2) return -1;
  return max(left_height, right_height) + 1;

}

bool isBalancedOptimized(Node* node) {
  if (getHeight(node) == -1) return false;
  return true;
}
