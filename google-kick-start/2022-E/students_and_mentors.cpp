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

int naive_max(vi ratings, int curr) {
    int limit = ratings[curr] * 2;
    int max_rating = -1;
    F0R(i, ratings.size()) {
        if (ratings[i] > max_rating && ratings[i] <= limit && i != curr) {
            max_rating = ratings[i];
        }
    }
    return max_rating;
}

void solve() {
    int num;
    vi ratings;

    cin >> num;

    int curr;
    F0R(i, num) {
        cin >> curr;
        ratings.pb(curr);
    }

    F0R(i, num) {
        cout << " " << naive_max(ratings, i);
    }

    cout << endl;

    // Naive non sorted

}

int T;

int main() {
    setIO("test");

    cin >> T;
    FOR(i, 1, T + 1) {
        cout << "Case #" << i << ":";
        solve();
    }

    return 0;
}
