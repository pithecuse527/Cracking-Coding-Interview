#include <iostream>
#include <vector>
#include "my_node.cpp"

using namespace std;

Node* minHeightTree(vector<int> arr, int l, int r) {
  if (l > r) return nullptr;  // important to use this rather than l==r
  int mid = (l+r) / 2;
  Node* root = new Node(arr[mid]);
  root->setLeft(minHeightTree(arr, l, mid-1));
  root->setRight(minHeightTree(arr, mid+1, r));

  return root;

}
