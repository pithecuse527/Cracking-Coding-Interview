// cracking the coding interview
// problem 4.9 - finding the route from n1 to n2

#include <iostream>
#include "my_node.cpp"

using namespace std;

// this assumes that *root is always a root of the binary tree
int findRoute1(Node* root, int val) {
  if (!root)
    return 0;

  int left_sum;
  int right_sum;
  int to_return = 0;

  if (root->getVal() == val)
    to_return += val;

  if ((left_sum = findRoute1(root->getLeft(), val)))
    to_return += left_sum;
  if ((right_sum = findRoute1(root->getRight(), val)))
    to_return += right_sum;

  return to_return;

}

int main() {
  Node n1(1);
  Node n2(0);
  Node n3(1);
  Node n4(1);
  Node n5(1);
  Node n6(1);
  Node n7(1);
  Node n8(1);

  n1.setLeft(&n2);
  n1.setRight(&n3);
  n2.setLeft(&n4);
  n2.setRight(&n5);
  n3.setLeft(&n6);
  n3.setRight(&n7);
  n5.setRight(&n8);

  cout << findRoute1(&n1, 1) << endl;

  return 0;
}
