#include <iostream>
#include <vector>
#include "my_node.cpp"

using namespace std;

bool isBST(Node* root, vector<int>& arr, int& i) {
  if (!root) return true;

  bool left = isBST(root->getLeft(), arr, i);
  arr.push_back(root->getVal());
  if (i > 0 && arr[i] <= arr[i-1]) return false;  // return false immediate
  i++;  // compare next
  bool right = isBST(root->getRight(), arr, i);

  if (!left || !right) return false;  // if it was not a BST return false
  return true;

}

int main() {
  Node* c0 = new Node(4);
  Node* c1 = new Node(2);
  Node* c2 = new Node(6);
  Node* c3 = new Node(1);
  Node* c4 = new Node(3);
  Node* c5 = new Node(5);
  Node* c6 = new Node(7);

  c0->setLeft(c1);
  c0->setRight(c2);
  c1->setLeft(c3);
  c1->setRight(c4);
  c2->setLeft(c5);
  c2->setRight(c6);

  vector<int> arr;
  int i = 0;

  cout << isBST(c0, arr, i) << endl;

  return 0;
}
