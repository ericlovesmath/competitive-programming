// Headers {{{
#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>
#include <iterator>
#include <map>
#include <math.h>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

void setIO(string name = "") {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    if (name.size()) {
        freopen((name + ".in").c_str(), "r", stdin);
        freopen((name + ".out").c_str(), "w", stdout);
    }
}

// Types
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef string str;

typedef pair<int, int> pi;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<ll> vll;

// Vectors
#define sz(x) int((x).size())
#define all(x) begin(x), end(x)
#define sortVec(x) sort(all(x))
#define pb push_back

// Loops
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define F0R(i, a) FOR(i, 0, a)
#define ROF(i, a, b) for (int i = (b)-1; i >= (a); --i)
#define R0F(i, a) ROF(i, 0, a)
#define foreach(a, x) for (auto &a : x)

// }}}

// Problem Statement {{{
// Link:
// https://codingcompetitions.withgoogle.com/kickstart/round/000000000043585c/000000000085a152
// }}}

void solve() {
    string inp;
    cin >> inp;

    vector<char> anagram;
    foreach (c, inp)
        anagram.pb(c);

    stack<int> swap_buffer;
    int temp;
    F0R(i, inp.size()) {
        if (swap_buffer.empty()) {
            swap_buffer.push(i);
            cout << "Pushed " << i << endl;
        } else if (anagram[swap_buffer.top()] != anagram[i]) {
            temp = anagram[swap_buffer.top()];
            anagram[swap_buffer.top()] = anagram[i];
            anagram[i] = temp;
            swap_buffer.pop();
        } else {
            swap_buffer.push(i);
            cout << "Pushed " << i << endl;
        }
    }

    foreach (c, anagram) {
        cout << c;
    }
    cout << endl;

    if (!swap_buffer.empty())
        cout << "IMPOSSIBLE" << endl;
    else {
        foreach (c, anagram) {
            cout << c;
        }
        cout << endl;
    }
}

int T;

int main() {
    setIO("test");

    cin >> T;
    FOR(i, 1, T + 1) {
        cout << "Case #" << i << ": ";
        solve();
    }

    return 0;
}
