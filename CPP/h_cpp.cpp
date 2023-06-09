#include <iostream>
#include <vector>
#include <fstream>
#include <set>
#include <algorithm>
#include <cmath>

std::vector<int> arr;
std::multiset<int> min_set;
std::multiset<int> max_set;

std::ifstream cin("input.txt");
std::ofstream cout("output.txt");

// void print() {
// 	std::cout << "[ ";
// 	for (auto &it : min_set) {
// 		std::cout << it << " ";
// 	}
//     std::cout << "- ";
// 	for (auto &it : max_set) {
// 		std::cout << it << " ";
// 	}
// 	std::cout << "] " << *min_set.rbegin() << std::endl;
// }

int main() {
	long long res = 0;
	int n;
	cin >> n;
	arr.resize(n, 0);
	for (size_t i = 0; i < n; ++i) {
		cin >> arr[i];
	}
	std::vector<int> sort_arr(arr);
	std::sort(sort_arr.begin(), sort_arr.end());

    int k = std::ceil(float(n) / 2);

	min_set.insert(sort_arr.begin(), sort_arr.begin() + k);
	max_set.insert(sort_arr.begin() + k, sort_arr.end());

    int del_num = 0;
    int num = 0;
    std::multiset<int>::iterator it;

    for (int i = 0; i < n; ++i) {
        if (min_set.size() < max_set.size()) {
            it = max_set.begin();
            min_set.insert(*it);
            max_set.erase(it);
        }
        else if (min_set.size() > max_set.size() + 1) {
            it = min_set.find(*min_set.rbegin());
            max_set.insert(*it);
            min_set.erase(it);
        }
        // print();
        num = *min_set.rbegin();
        res += num;
        del_num = arr.back();
        arr.pop_back();
        if (del_num <= *min_set.rbegin()) {
            it = min_set.find(del_num);
            min_set.erase(it);
        }
        else {
            it = max_set.find(del_num);
            max_set.erase(it);
        }
    }
	std::cout << res << std::endl;
}
