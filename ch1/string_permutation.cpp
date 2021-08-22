#include <algorithm>
#include <string>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  bool solution1(string& s1, string& s2) {    // we assume there is no whitespace and only consider
                                              // the low chars.
    if (s1.size() != s2.size()) return false;

    // sort first
    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());

    if (s1.compare(s2) == 0) {
      return true;
    }

    return false;
  }
};

int main() {
  string s1 = "helloworld";
  string s2;
  Solution s;

  cin >> s2;
  cout << s.solution1(s1, s2) << endl;

  return 0;
}
