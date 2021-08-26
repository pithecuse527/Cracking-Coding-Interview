#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
  bool solve(string s1, string s2) {
    if (s1.size() == s2.size()) { // no need to check s1 and s2 has differnt size
      string s1s1 = s1+s1;
      return s1s1.find(s2, 0) != string::npos;  // is s2 substring of s1s1?
    }

    return false;
  }
};

int main() {
  string s1;
  string s2;
  Solution s;

  cin >> s1 >> s2;
  cout << s.solve(s1, s2) << endl;

  return 0;
}
