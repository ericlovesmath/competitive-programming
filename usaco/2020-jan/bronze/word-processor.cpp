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

// Essay: N words, separated by spaces
//      1 <= N <= 100
// Word: 1 to 15 characters long, only upper/lowercase
// Each line is max K chars long (not counting spaces)
//      1 <= K <= 80
//
// No space at the end of a line, format essay

// }}}

int N, K;
int curr_len;
string word;

int main() {

    setIO("word");

    cin >> N >> K;

    // First Word
    cin >> word;
    curr_len = word.size();
    cout << word;

    for (int i = 1; i < N; i++) {

        cin >> word;
        if (curr_len + word.size() > K) {
            cout << endl << word;
            curr_len = word.size();
        } else {
            cout << ' ' << word;
            curr_len += word.size();
        }
    }
}
