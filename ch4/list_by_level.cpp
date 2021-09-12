#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// node for tree
class TreeNode {
public:
  vector<TreeNode*> children;
  int val;
};

// node for linked list
class Node {
public:
  Node* next = nullptr;
  int val = -1;
};

vector<Node*> createLinkedLists(TreeNode* root) {
  vector<Node*> to_return;
  queue<TreeNode*> q;
  Node* runner = nullptr; // runner for the linked list
  Node* head = nullptr; // head of the linked list
  int current_q_size;

  q.push(root);
  while(!q.empty()) {
    current_q_size = q.size();

    // dequeue everything and create the linked list
    for (int i=0; i<current_q_size; i++) {
      // on the first dequeue of the level
      if (!head) {
        head = new Node();
        head->val = q.front()->val;
        runner = head;
        to_return.push_back(head);
      }
      else {  // the head already exist and pushed,
        runner->next = new Node();
        runner = runner->next;
        runner->val = q.front()->val;
      }

      // enqueue for the next level (BFS)
      for (int j=0; j<(q.front()->children).size(); j++) {
        q.push(q.front()->children[j]);
      }
      q.pop();  // dequeue the front
    }

    // reset head and runner for the next level
    head = nullptr;
    runner = nullptr;
  }

  return to_return;
}

int main() {
  // testing binary tree
  TreeNode c0;
  c0.val = 0;
  TreeNode c1;
  c1.val = 1;
  TreeNode c2;
  c2.val = 2;
  TreeNode c3;
  c3.val = 3;
  TreeNode c4;
  c4.val = 4;
  TreeNode c5;
  c5.val = 5;
  TreeNode c6;
  c6.val = 6;
  TreeNode c7;
  c7.val = 7;

  c0.children.push_back(&c1);
  c0.children.push_back(&c2);
  c1.children.push_back(&c3);
  c1.children.push_back(&c4);
  c2.children.push_back(&c5);
  c2.children.push_back(&c6);
  c3.children.push_back(&c7);

  vector<Node*> result = createLinkedLists(&c0);
  Node* runner;

  for (int i=0; i<result.size(); i++) {
    runner = result[i];
    while(runner) {
      cout << runner->val << endl;
      runner = runner->next;
    }
    cout << endl;
  }

  return 0;
}
