// Headers {{{
#include <algorithm>
#include <array>
#include <iostream>
#include <iterator>
#include <map>
#include <math.h>
#include <queue>
#include <set>
#include <string>
#include <tuple>
#include <unordered_map>
#include <vector>

using namespace std;
#define endl '\n'

void setIO(string name = "") {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    if (name.size()) {
        freopen((name + ".in").c_str(), "r", stdin);
        freopen((name + ".out").c_str(), "w", stdout);
    }
}
// }}}

// Problem Statement {{{

// http://www.usaco.org/index.php?page=viewproblem2&cpid=664

// N Spelling boards, 1 <= N <= 100
// Each board has a word on each side
// How many of each letter do you need to make every word, when only one is face
// up?

// }}}

// Initialize freq_map

int freq_all[26] = {};
string w1, w2;

int main() {

    setIO("blocks");

    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {

        int freq_1[26] = {};
        int freq_2[26] = {};
        cin >> w1 >> w2;

        for (char c : w1) {
            freq_1[int(c - 'a')]++;
        }
        for (char c : w2) {
            freq_2[int(c - 'a')]++;
        }

        for (int j = 0; j < 26; j++) {
            freq_all[j] += max(freq_1[j], freq_2[j]);
        }
    }

    for (int num : freq_all) {
        cout << num << endl;
    }
}
