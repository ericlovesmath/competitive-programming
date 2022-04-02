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

// N = num dice in game
// S_1 to S_N = number of sides in each die

// }}}

int T, N, new_dice;
vector<int> dice;

void solve() {

    cin >> T;

    for (int t = 0; t < T; ++t) {

        cout << "Case #" << t + 1 << ": ";
        cin >> N;

        dice.clear();
        for (int i = 0; i < N; ++i) {
            cin >> new_dice;
            dice.push_back(new_dice);
        }

        int max_len = 0;
        sort(dice.begin(), dice.end());
        for (int i = 0; i < dice.size(); ++i) {
            if (dice[i] > max_len) {
                max_len++;
            }
        }

        cout << max_len << endl;

    }
}

int main() {
    setIO("test");
    solve();
}
