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

// 3 printers
// Printing a d takes 10^6 units in total of CMYK
// Given an ink in each printer, output any CMYK that can be printed by all 3

// }}}

int T;
int c[4];

void solve() {

    cin >> T;

    for (int t = 0; t < T; ++t) {
        int max_c[4] = {1000001, 1000001, 1000001, 1000001};

        for (int i = 0; i < 3; ++i) {
            cin >> c[0] >> c[1] >> c[2] >> c[3];
            for (int j = 0; j < 4; ++j) {
                if (c[j] < max_c[j]) {
                    max_c[j] = c[j];
                }
            }
        }

        cout << "Case #" << t + 1 << ": ";

        int excess = max_c[0] + max_c[1] + max_c[2] + max_c[3] - 1000000;
        if (excess < 0) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            int index = 0;
            while (excess > 0) {
                if (excess <= max_c[index]) {
                    max_c[index] -= excess;
                    excess = 0;
                } else {
                    excess -= max_c[index];
                    max_c[index] = 0;
                    index++;
                }
            }

            cout << max_c[0] << " ";
            cout << max_c[1] << " ";
            cout << max_c[2] << " ";
            cout << max_c[3] << " " << endl;
        }
    }
}

int main() {
    setIO("test");
    solve();
}
