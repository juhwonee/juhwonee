#include <iostream>
using namespace std;

int main() {
	int T, H, W, N;
	int floor, room, num, answer[100];

	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> H >> W >> N;

		floor = N % H;
		room = N / H + 1;

		if (floor == 0) {
			floor = H;
			room = N / H;
		}
	
		num = floor * 100 + room;
		answer[i] = num;
	}

	for (int i = 0; i < T; i++) {
		cout << answer[i] << '\n';
	}

	
	return 0;
}