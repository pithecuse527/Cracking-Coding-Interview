#include <iostream>
// #include <queue>
#include <vector>
#include "my_node.cpp"

using namespace std;

bool isThereAWay(Node* from, Node* to) {
  Node *left, *right;
  // queue<Node*> q;
  vector<Node> q;

  q.push_back(*from);

  do {
    Node runner = q[0]; // tmp runner object
    if (!runner.getVisited()) { // if the node has not visited
      runner.setVisited(true);
      if ( (left=runner.getLeft()) )
        q.push_back(*left);
      if ( (right=runner.getRight()) )
        q.push_back(*right);
    }
    q.erase(q.begin()); // dequeue from the queue

    if (runner.getVal() == to->getVal()) return true;

  } while (!q.empty());

  return false;

}

int main() {
  Node n1(1);
  Node n2(2);
  Node n3(3);
  Node n4(4);
  Node n5(5);
  Node n6(6);
  Node n7(7);
  Node n8(8);

  n1.setLeft(&n3);
  n1.setRight(&n2);
  n2.setLeft(&n7);
  n3.setLeft(&n4);
  n3.setRight(&n7);
  n4.setLeft(&n6);
  n4.setRight(&n5);

  cout << isThereAWay(&n1, &n7) << endl;

  return 0;
}
