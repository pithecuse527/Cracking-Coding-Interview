#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
  void solve(string& target) {
    int space_cnt = 0;
    int cur_len = target.size();
    int new_len;
    int new_len_runner;

    for (int i=0; i<cur_len; i++) {
      if (target[i] == ' ') {
        space_cnt++;
      }
    }
    new_len = cur_len + space_cnt * 2;  // how much we expand? (think about why space*2)
    target.resize(new_len, '0');  // exapnd the string with char '0'
    target[new_len] = '\0'; // end of the string
    new_len_runner = new_len - 1; // runner for the new expanded length

    for (int i=cur_len-1; i > -1; i--) {
      if (target[i] == ' ') { // whitespace
        target[new_len_runner] = '0';
        target[new_len_runner-1] = '2';
        target[new_len_runner-2] = '%';
        new_len_runner -= 3;
      }
      else {    // normal char.
        target[new_len_runner--] = target[i];
      }
    } // for
  } // method
};

int main() {
  Solution s;
  string str = "Hello world! It is me!";
  cout << str << endl;
  s.solve(str);
  cout << str << endl;

  return 0;
}
