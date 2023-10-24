#include <iostream>

/*
PADINGROME

see if it's a padingrome

g++ padingrome.cpp -o out/padingrome
out/padingrome

g++ padingrome.cpp -o linout/padingrome
linout/padingrome


*/

class solution {
public:
	static bool padingrome(int x) {
		if (x < 0) return false;

		int cut = 1;
		while (x >= 10 * cut) {
			cut *= 10;
		};
		// if x is 19, make it 10
		// if x is 1342, make it 1000


		while (x) {
			int left = x / cut; //floors the cut division, moves the num the num of zeros
			int right = x % 10; //cuts off everything after ones place

			if (left != right) return false; //compares

			x = (x % cut) / 10; //cuts off the left (ex 1323 %1000 = 323) then the right (323 /10 = 23)


			cut /= 100; //cuts off 2 zeros (for both left and right)
		};
		return true;

	};

};

int main() {
	std::cout << solution::padingrome(101) << '\n';
	std::cout << solution::padingrome(10382) << '\n';
	std::cout << solution::padingrome(10) << '\n';
	std::cout << solution::padingrome(0) << '\n';


}