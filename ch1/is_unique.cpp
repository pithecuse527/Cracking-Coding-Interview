#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

class Solution {
public:
  bool solve1(string str) { // brute force solution with hash map
    unordered_map<char, int> hash_map;

    for (char c : str) {
      if (hash_map.find(c) == hash_map.end()) {
        hash_map[c]++;
      }
      else {
        return false;
      }
    }
    return true;
  }

  bool solve2(string str) { // elegant way by using bit array
    if (str.size() > 26) return false;

    int bit_arr = 0;  // bit array
    int adder;  // indicator of a char
    for (char ch : str) {
      adder = 1 << (ch - 'a');  // find the location to add
      if ((bit_arr & adder) > 0) {  // if the location is already filled
        return false;
      }
      else {
        bit_arr |= adder; // fill the location
      }
    }

    return true;
  }
};

int main() {
  string str = "abcdefghijk";
  Solution s;

  cout << s.solve1(str) << endl;
  cout << s.solve2(str) << endl;

  return 0;
}
