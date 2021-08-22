#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
  void solve(string& str) {
    int str_size = str.size();
    for (int i=0; i<str_size/2; i++) {
      swap(str[i], str[str_size-1-i]);
    }
  }
};

int main() {
  string str = "helloWorld!!";
  Solution s;

  cout << str << endl;
  s.solve(str);
  cout << str << endl;
  return 0;
}
