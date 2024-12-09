//#include "aoc01.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <cstdint>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <set>
#include <unordered_set>

int main() {

    // read input
    std::ifstream input_fs("../input");
    if (!input_fs.is_open()) exit(1);

    std::string line;
    std::vector<long long> left, right;
    left.reserve(100);
    right.reserve(100);
    while (std::getline(input_fs, line)) {
        auto ss = std::stringstream(line);
        long long r, l;
        ss >> l >> r;
        left.push_back(l);
        right.push_back(r);
    }

    std::sort(left.begin(), left.end());
    std::sort(right.begin(), right.end());

    auto result = std::inner_product(left.begin(), left.end(), right.begin(), 0, std::plus<long long>(),[&](long long a, long long b) {return std::abs(a-b);});

    std::cout << result << std::endl;
	auto counter = std::unordered_multiset<long long>(right.begin(), right.end());
    long long sum = 0;
    for (auto &num: std::unordered_set(left.begin(), left.end())) {
    	sum += num * counter.count(num);
    }
	std::cout << sum << std::endl;
    return 0;
}