#include <iostream>
#include "my_node.cpp"

using namespace std;

Node* veryLeftNode(Node* n) { // return the very left node of right subtree
  Node* very_left_node = n;
  while(very_left_node->getLeft()) // going down until it is the very left child
    very_left_node = very_left_node->getLeft();
  return very_left_node;
}

Node* nextSuccInorder(Node* to_find) {  // the next node of inorder traversal
  Node* nextNode = to_find;

  // if there is no right subtree,
  if(!(to_find->getRight())) {
    // going up until it reaches to the root, or
    // we found the parent that its right subtree has not been visited
    while(nextNode->getParent()) {
      nextNode = nextNode->getParent();
      if(!(nextNode->getRight()->getVisited())) break;
    }
  }
  // if there is a right subtree, found nextNode from the right subtree
  else nextNode = veryLeftNode(to_find->getRight());

  // if nextNode reaches to the root, it means no further node on n
  if(!(nextNode->getParent())) nextNode = nullptr;

  return nextNode;
}
