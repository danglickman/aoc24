#include <iostream>
#include <fstream>
#include <vector>
#include <cstdint>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <map>
#include <optional>
#include <set>
#include <unordered_map>
#include <unordered_set>

std::optional<std::pair<uint64_t, uint64_t>> even_digits(uint64_t number) {
    if (number == 0) return std::make_pair(0, 0);
    uint64_t a, b;
    a = b = 0;
    std::vector<uint64_t> digits;
    while (number != 0) {
        digits.push_back(number % 10);
        number /= 10;
    }

    if (digits.size() % 2 != 0) {
        return {};
    }

    std::reverse(digits.begin(), digits.end());
    for (auto i = 0; i < digits.size()/2; i++) {
        a *= 10;
        a += digits[i];
    }
    for (auto i = digits.size()/2; i < digits.size(); i++) {
        b *= 10;
        b += digits[i];
    }
    return std::make_pair(a, b);


}

int main() {

    // read input
    std::ifstream input_fs("input");
    if (!input_fs.is_open()) exit(1);
    std::string line;


    std::unordered_map<uint64_t, uint64_t> stones;
    std::unordered_map<uint64_t, uint64_t> next_stones;

    while (std::getline(input_fs, line)) {
        auto ss = std::stringstream(line);
        uint64_t a;
        while (ss >> a) {
            stones[a]++;
        }
    }

    constexpr uint64_t blinks = 75;

    // # 0 -> 1
    // # no_digits even -> split in half
    // # else: mult by 2024
    for (auto i = 0; i < blinks; i++) {
        // std::cout << "Blink: " << i << std::endl;
        // for (auto& stone : stones) {
        //     std::cout << "(" << stone.first << ":" << stone.second << "), " ;
        // }
        // std::cout << std::endl;
        for (auto& stone : stones) {

            // std::cout << stone.first << " " << stone.second << std::endl;
            if (stone.first == 0) {
                if (next_stones.contains(stone.first)) {
                    next_stones[1] += stone.second;
                } else {
                    next_stones[1] = stone.second;
                }
            } else if (auto result = even_digits(stone.first)) {
                auto parts = result.value();
                if (next_stones.contains(parts.first)) {
                    next_stones[parts.first] += stone.second;
                } else {
                    next_stones[parts.first] = stone.second;
                }
                if (next_stones.contains(parts.second)) {
                    next_stones[parts.second] += stone.second;
                } else {
                    next_stones[parts.second] = stone.second;
                }
            } else {
                auto new_value = stone.first * 2024;
                if (next_stones.contains(new_value)) {
                    next_stones[new_value] += stone.second;
                } else {
                    next_stones[new_value] = stone.second;
                }
            }

        }
        std::swap(stones, next_stones);
        next_stones.clear();

    }

    uint64_t sum = 0;
    for (auto& stone : stones) {
        sum += stone.second;
    }
    std::cout << sum << std::endl;




    return 0;
}