// subsets.cpp

#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

// Functions

size_t subsets(vector<int> &s, vector<int> &d, size_t k) {
    if (k == d.size()) { // Base: have complete subset
    	// for (auto e : s) { cout << " " << e; }; cout << endl;
    	return (accumulate(s.begin(), s.end(), 0) % 3 == 0) ? 1 : 0;
    }

    size_t count = 0;

    // Recurse: skip current
    count += subsets(s, d, k + 1);

    // Recurse: with current
    s.push_back(d[k]);
    count += subsets(s, d, k + 1);
    s.pop_back(); // Reset subset
    
    return count;
}

// Main execution

int main(int argc, char *argv[]) {
    vector<int> subset;
    vector<int> numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    size_t      count   = subsets(subset, numbers, 0);

    cout << count << endl;
    return 0;
}
