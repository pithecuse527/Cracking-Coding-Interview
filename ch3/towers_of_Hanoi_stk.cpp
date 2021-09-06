#include <iostream>
#include <stack>

using namespace std;

// mover every plates from tower1 to tower3
void hanoi(int plates, stack<int>& tower1, stack<int>& tower2, stack<int>& tower3) {
  // base case
  if (plates <= 0) return;

  // use tower3 as a buffer to move n-1 plates from tower1 to tower2
  hanoi(plates-1, tower1, tower3, tower2);

  // move the last plate from tower1 to tower3
  tower3.push(tower1.top());
  tower1.pop();

  // move every plates from tower2 to tower3 using tower1 as a buffer
  hanoi(plates-1, tower2, tower1, tower3);
}

int main() {
  stack<int> tower1;
  stack<int> tower2;
  stack<int> tower3;

  int i;
  int tmp;
  cin >> i;
  tmp = i;

  for(; i>=1; i--) {
    tower1.push(i);
  }
  hanoi(tmp, tower1, tower2, tower3);

  for(; tmp>=1; tmp--) {
    cout << tower3.top() << endl;
    tower3.pop();
  }
  return 0;
}
