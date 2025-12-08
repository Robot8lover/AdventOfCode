#include <array>
#include <fstream>
#include <iostream>
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

void do_case(string filename, bool sample) {
    cout << "Running " << filename << endl;
    vector<string> lines = read_lines(filename);
    long long total = 0;
    for (string line : lines) {
        int hyphen = line.find("-");
        long long start = stoll(line.substr(0, hyphen));
        long long end = stoll(line.substr(hyphen + 1));
        for (int num = start; num <= end; ++num) {
            int remaining_num = num;
            array<bool, 10> seen = {false, false, false, false, false, false, false, false, false, false};
            while (remaining_num > 0) {
                int digit = remaining_num % 10;
                if (seen[digit]) {
                    if (sample) {
                        cout << num << endl;
                    }
                    total += num;
                    break;
                } else {
                    seen[digit] = true;
                }
                remaining_num /= 10;
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
