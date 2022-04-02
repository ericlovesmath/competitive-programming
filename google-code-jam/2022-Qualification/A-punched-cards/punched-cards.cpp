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

int T, R, C;

string edge(int length) {
    string border = "+";
    for (int i = 0; i < length; ++i) {
        border += "-+";
    }
    return border;
}

string cell(int length) {
    string border = "|";
    for (int i = 0; i < length; ++i) {
        border += ".|";
    }
    return border;
}

void solve() {

    cin >> T;

    for (int t = 0; t < T; ++t) {
        cin >> R >> C;

        cout << "Case #" << t + 1 << ":" << endl;
        cout << ".." << edge(C - 1) << endl;
        cout << ".." << cell(C - 1) << endl;
        string walls = edge(C);
        string cells = cell(C);
        for (int r = 1; r < R; ++r) {
            cout << walls << endl << cells << endl;
        }
        cout << walls << endl;
    }
}

int main() {

    setIO("test");
    solve();
}
