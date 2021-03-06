class Node {
public:
  Node(int v) {
    val = v;
    left = nullptr;
    right = nullptr;
    visited = false;
    parent = nullptr;
  }

  // setting the value
  void setVal(int v) {
    val = v;
  }

  // getting the value
  int getVal() {
    return val;
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

  // setting visited info.
  void setVisited(bool b) {
    visited = b;
  }

  // getting visited info.
  bool getVisited() {
    return visited;
  }

  // setting the parent node
  void setParent(Node* n) {
    parent = n;
  }

  // getting the parent node
  Node* getParent() {
    return parent;
  }

private:
  Node* left;
  Node* right;
  int val;
  bool visited;
  Node* parent;
};
