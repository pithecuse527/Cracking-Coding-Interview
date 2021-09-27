#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool is_contain(const vector<int>& numbers, int n) {
	for (auto num : numbers) {
		if (n == num)
			return true;
	}
	return false;
}

void permutation(vector<int>& numbers, vector<int> card, int pvt) {
	if (pvt == card.size()-1) {
		string to_pushed = "";
		for (int i=0; i<card.size(); i++) {
			to_pushed += (to_string(card[i]));
		}
		if (!is_contain(numbers, stoi(to_pushed)))
			numbers.push_back(stoi(to_pushed));
		return;
	}

	if (pvt+1 <= card.size()-1) {
		permutation(numbers, card, pvt+1);
		for (int i=pvt+1; i<card.size(); i++) {
			swap(card[i], card[pvt]);
			permutation(numbers, card, pvt+1);
			swap(card[i], card[pvt]);
		}
	}

}

int solution(vector<int> card, int n) {
    // 여기에 코드를 작성해주세요.
    int answer = 0;
		vector<int> numbers;
		permutation(numbers, card, 0);

		sort(numbers.begin(), numbers.end());
		for (; answer<numbers.size(); answer++)
			if (numbers[answer] == n)
				break;

    // cout << numbers.size() << endl;

		if (answer == numbers.size())
			return -1;

    return answer+1;
}

int main() {
    // vector<int> card1 = {1, 2, 1, 3};
    // int n1 = 1312;
    // int ret1 = solution(card1, n1);
    //
    // // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    // cout << "solution 함수의 반환 값은 " << ret1 << " 입니다." << endl;

    vector<int> card2 = {1, 1, 1, 2};
    int n2 = 1122;
    int ret2 = solution(card2, n2);

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    cout << "solution 함수의 반환 값은 " << ret2 << " 입니다." << endl;
}
