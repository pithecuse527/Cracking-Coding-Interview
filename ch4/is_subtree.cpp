#include <iostream>
#include <queue>
#include "my_node.cpp"

using namespace std;

// check whether it is subtree or not by using BFS
bool check(Node* t1, Node* t2) {
  queue<Node*> q1;
  queue<Node*> q2;
  q1.push(t1);
  q2.push(t2);

  Node* runner1;
  Node* runner2;

  while (!q2.empty()) {
    runner1 = q1.front();
    runner2 = q2.front();
    if (runner1->getVal() != runner2->getVal())
      return false;

    // add left child node if exist
    if (runner1->getLeft())
      q1.push(runner1->getLeft());
    if (runner2->getLeft())
      q2.push(runner2->getLeft());

    // it is possible that q1 pushed the left child but
    // q2 not pushed the left child as there is nothing to be pushed.
    // This may be possible that t1 is larger than t2, so we need to push
    // the left child of runner1 to q2 to give the answer properly.
    if (q1.size() != q2.size()) q2.push(runner1->getLeft());

    // add right child node if exist
    if (runner1->getRight())
      q1.push(runner1->getRight());
    if (runner2->getRight())
      q2.push(runner2->getRight());

    // same for the right child
    if (q1.size() != q2.size()) q2.push(runner1->getRight());

    q1.pop();
    q2.pop();

  }

  return true;
}

// is t2 subtree of t1?
bool isSubtree(Node* t1, Node* t2) {
  if (!t2) return true;
  if (!t1) return false;

  // start to check when the root is same
  if (t1->getVal() == t2->getVal()) {
    return check(t1, t2);
  }

  return (isSubtree(t1->getLeft(), t2) || isSubtree(t1->getRight(), t2));
}

int main() {
  Node n0(0);
  Node n1(1);
  Node n2(2);
  Node n3(3);
  Node n4(4);
  Node n5(5);
  Node n6(6);
  Node n7(7);

  n0.setLeft(&n1);
  n0.setRight(&n2);
  n1.setLeft(&n3);
  n1.setRight(&n4);
  n2.setLeft(&n5);
  n2.setRight(&n6);
  n3.setLeft(&n7);

  Node n00(0);
  Node n10(1);
  Node n20(2);
  Node n40(5);

  n00.setLeft(&n10);
  n00.setRight(&n20);
  n10.setRight(&n40);

  cout << isSubtree(&n0, &n00) << endl;

  return 0;
}
