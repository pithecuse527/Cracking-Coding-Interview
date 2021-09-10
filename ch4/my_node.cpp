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
