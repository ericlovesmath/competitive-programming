// Headers {{{
#include <algorithm>
#include <iostream>
#include <iterator>
#include <map>
#include <math.h>
#include <queue>
#include <set>
#include <string>
#include <tuple>
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

// Print the pattern

// }}}

int T;

void solve() {

    string word;
    string min_word = "";
    string test_1 = "";
    string test_2 = "";
    cin >> word;
    for (int i = 0; i < word.size(); ++i) {
        test_1 = min_word + word[i] + word.substr(i);
        test_2 = min_word + word[i] + word[i] + word.substr(i);
        if (test_1 < test_2) {
            min_word = min_word + word[i];
        } else {
            min_word = min_word + word[i] + word[i];
        }
    }
    cout << min_word << endl;
}

int main() {

    setIO("test");
    cin >> T;
    for (int t = 0; t < T; ++t) {
        cout << "Case #" << t + 1 << ": ";
        solve();
    }
}
