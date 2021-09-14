#include <iostream>
#include "my_node.cpp"

using namespace std;

// when we have an access to the parent node (bottom-up)
Node* firstVersion(Node* root, Node* n1, Node* n2) {
  Node* runner1;  // first runner going up to the root
  Node* runner2;  // second runner going up to the root

  runner1 = n1;
  runner2 = n2;
  while (runner1->getParent()) {
    runner1->setVisited(true);
    runner1 = runner1->getParent();
  }
  runner1->setVisited(true);

  // second runner will stop going up when it reaches to the root,
  // or when it meets the first visited parent node by first runner
  while (runner2->getParent() && !(runner2->getVisited())) {
    runner2 = runner2->getParent();
  }
  return runner2;

}

bool nodeInSubtree(Node* subTreeRoot, Node* to_find) {
  if (!subTreeRoot) return false; // have not found
  if (subTreeRoot == to_find) return true;
  bool exist_on_left = nodeInSubtree(subTreeRoot->getLeft(), to_find);
  bool exist_on_right = nodeInSubtree(subTreeRoot->getRight(), to_find);

  if (exist_on_left || exist_on_right) return true;
  return false;

}

// when we do not have an access to the parent node (top-down)
// we also assume the n1 and n2 always exist in the tree
Node* secondVersion(Node* root, Node* n1, Node* n2) {
  Node* common_ancestor_ = root;
  bool n1_in_left = nodeInSubtree(common_ancestor_->getLeft(), n1);
  bool n2_in_left = nodeInSubtree(common_ancestor_->getLeft(), n2);

  while(common_ancestor_ && n1_in_left && n2_in_left) {
    if (n1_in_left && n2_in_left) common_ancestor_ = common_ancestor_->getLeft();
    if (!n1_in_left && !n2_in_left) common_ancestor_ = common_ancestor_->getRight();

    n1_in_left = nodeInSubtree(common_ancestor_->getLeft(), n1);
    n2_in_left = nodeInSubtree(common_ancestor_->getLeft(), n2);

  }

  // as we assume n1 and n2 is in the tree, this won't happen
  return common_ancestor_;
}

int main() {
  Node n1(1);
  Node n2(2);
  Node n3(3);
  Node n4(4);
  Node n5(5);
  Node n6(6);
  Node n7(7);

  n1.setLeft(&n3);
  n1.setRight(&n2);
  n3.setLeft(&n4);
  n3.setRight(&n7);
  n4.setLeft(&n6);
  n4.setRight(&n5);

  n4.setParent(&n3);
  n3.setParent(&n1);
  n7.setParent(&n3);
  n5.setParent(&n4);


  Node* common_ancestor_1 = firstVersion(&n1, &n5, &n7);
  Node* common_ancestor_2 = secondVersion(&n1, &n5, &n7);

  cout << common_ancestor_1->getVal() << endl;
  cout << common_ancestor_2->getVal() << endl;

  return 0;
}
