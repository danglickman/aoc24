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
    digits.reserve(16);
    while (number != 0) {
        digits.push_back(number % 10);
        number /= 10;
    }

    if (digits.size() % 2 != 0) {
        return {};
    }

    std::ranges::reverse(digits);
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

struct PairHash
{
    template <class T1, class T2>
    std::size_t operator() (const std::pair<T1, T2> &v) const
    {
        return std::hash<T1>()(v.first) ^ std::hash<T2>()(v.second) << 1;
        //return std::hash<T1>{}(v.first) ^ hash<T2>{}(v.second) << 1;    //same as above
    }
};

std::uint64_t stone_count(uint64_t stone, uint64_t blinks) {
    //  to use unordered map need hash object. this is probably faster
    static std::unordered_map<std::pair<uint64_t, uint64_t>, uint64_t, PairHash> stone_counts;
    if (stone_counts.contains({stone, blinks})) {
        return stone_counts[{stone, blinks}];
    }
    uint64_t count = 0;
    if (blinks == 0) {
        count = 1;
    } else if (stone == 0) {
        count = stone_count(1, blinks-1);
    } else if (auto result = even_digits(stone)) {
        auto parts = result.value();
        count += stone_count(parts.first, blinks-1);
        count += stone_count(parts.second, blinks-1);
    } else {
        auto new_value = stone * 2024;
        count += stone_count(new_value, blinks-1);
    }
    stone_counts[std::make_pair(stone, blinks)] = count;
    return count;
}


void first_solution(std::map<uint64_t, uint64_t> &stones, uint64_t blinks) {
    // # 0 -> 1
    // # no_digits even -> split in half
    // # else: mult by 2024
    std::map<uint64_t, uint64_t> next_stones;
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

}


int main() {

    // read input
    std::ifstream input_fs("input");
    if (!input_fs.is_open()) exit(1);
    std::string line;

    // Unordered map breaks this somehow (I have no idea how/why)
    // could be that I have a bug that depends on iteration order?
    //
    std::map<uint64_t, uint64_t> stones;
    // std::vector<uint64_t> stone_list;

    while (std::getline(input_fs, line)) {
        auto ss = std::stringstream(line);
        uint64_t a;
        while (ss >> a) {
            stones[a]++;
            // stone_list.push_back(a);
        }
    }

    constexpr uint64_t blinks = 75;



    first_solution(stones, blinks);


    // for (auto& stone : stones) {
    //     std::cout << "(" << stone.first << ":" << stone.second << ")\n " ;
    // }

    uint64_t sum = 0;
    for (auto& stone : stones) {
        sum += stone.second;
    }

    //
    // uint64_t sum = 0;
    // for (auto stone : stone_list) {
    //     sum += stone_count(stone, blinks);
    // }

    std::cout << sum << std::endl;


    return 0;
}