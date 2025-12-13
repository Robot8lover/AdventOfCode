#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;

vector<string> read_lines(string filename) {
    ifstream input(filename);
    vector<string> lines;
    for (string line; getline(input, line, ',');) {
        lines.push_back(line);
    }
    return lines;
}

long long pow(long long base, long long exp) {
    if (exp < 0) {
        throw invalid_argument("exp cannot be negative");
    } else if (exp == 0) {
        return 1;
    } else {
        if (exp & 1) {
            // odd exponent
            return base * pow(base * base, exp >> 1);
        } else {
            // even exponent
            return pow(base * base, exp >> 1);
        }
    }
}

void do_case(string filename, bool sample) {
    cout << "Running " << filename << endl;
    vector<string> lines = read_lines(filename);
    long long total = 0;
    for (string line : lines) {
        int hyphen = line.find("-");
        long long start = stoll(line.substr(0, hyphen));
        long long end = stoll(line.substr(hyphen + 1));
        for (long long num = start; num <= end; ++num) {
            int digits = 0;
            long long remaining_num = num;
            while (remaining_num > 0) {
                ++digits;
                remaining_num /= 10l;
            }
            if (digits & 1) {
                // shortcut if odd
                continue;
            }
            long long mask = pow(10l, digits >> 1);
            if ((num % mask) == (num / mask)) {
                total += num;
            }
        }
    }
    cout << total << endl;
}

void do_case(string filename) {
    do_case(filename, false);
}

int main() {
    do_case("sample.txt", true);
    do_case("input.txt", false);

    return 0;
}
