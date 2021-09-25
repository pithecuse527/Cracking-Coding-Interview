#include <iostream>
#include <vector>
#include <string>

using namespace std;

void permutation(vector<string>& target, vector<char> numbers, int pvt_idx) {
  if (pvt_idx+1 == numbers.size()-1) {
    string *tmp = new string();
    for (int i=0; i<numbers.size(); i++)
      tmp->push_back(numbers[i]);

    target.push_back(*tmp);
    swap(numbers[pvt_idx], numbers[pvt_idx+1]);
    tmp = new string();
    for (int i=0; i<numbers.size(); i++)
      tmp->push_back(numbers[i]);
    target.push_back(*tmp);
    return;
  }

  permutation(target, numbers, pvt_idx+1);
  for (int i=pvt_idx+1; i<numbers.size(); i++) {
    swap(numbers[i], numbers[pvt_idx]);
    permutation(target, numbers, pvt_idx+1);
    swap(numbers[i], numbers[pvt_idx]);
  }

}

int main() {
  vector<char> test = {'1','2','3','4'};
  vector<string> result;

  permutation(result, test, 0);
  for (auto str : result) {
      cout << str << endl;
  }
  cout << result.size() << endl;

}
