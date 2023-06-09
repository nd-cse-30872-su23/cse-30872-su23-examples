// Exercise 03-B: Largest Number

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

// Functions

bool read_numbers(vector<string> &numbers) {
    numbers.clear();

    string line;
    if (getline(cin, line)) {
    	stringstream ss(line);
    	string n;
    	while (ss >> n) {
    	    numbers.push_back(n);
	}
    }

    return numbers.size();
}

// Main Execution

int main(int argc, char *argv[]) {
    vector<string> numbers;

    while (read_numbers(numbers)) {
    	sort(numbers.begin(), numbers.end(), [](const string &a, const string &b) {
    	    return stoi(a + b) > stoi(b + a);
	});

	for (auto n : numbers) {
	    cout << n;
	}
	cout << endl;
    }

    return 0;
}
