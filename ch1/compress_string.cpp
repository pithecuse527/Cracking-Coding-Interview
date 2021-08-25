#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
  int calculateNewSize(string str) {  // returns the new compressed string size
    int new_size = 0;
    auto runner = str.begin()+1; // we assume the string size is more than 2
    char pivot = str[0];
    int count = 1;

    while (*runner) {
      if (*runner != pivot) {
        pivot = *runner;
        new_size += to_string(count).size() + 1;
        count = 1;
      }
      else count++;

      runner++;
    }

    new_size += to_string(count).size() + 1;  // for the last consecutive chars
    return new_size;
  }

  string solve(string str) {
    int prev_size = str.size();
    int new_size = calculateNewSize(str); // calculate this prior to make the result string
    int count = 0;
    char pivot = str[0];
    int new_runner = 0;

    // create the result string first (full of '0')
    string result = "";
    result.resize(new_size, '0');

    if (new_size >= prev_size) return str;

    // insert the pivot and count char one by one
    for (char c : str) {
      if (c != pivot) {
        result[new_runner++] = pivot;
        for (char ci : to_string(count)) result[new_runner++] = ci;
        pivot = c;
        count = 1;
      }
      else count++;
    }

    // append the remaining pivot and the count
    result[new_runner++] = pivot;
    for (char ci : to_string(count)) result[new_runner++] = ci;

    return result;
  }
};

int main() {
  Solution s;
  string str;
  cin >> str;

  cout << s.solve(str) << endl;

  return 0;
}
