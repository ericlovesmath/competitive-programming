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
#include <string>
#include <tuple>
#include <vector>

using namespace std;

void setIO(string name = "") {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
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

// Kosaraju's Algorithm {{{

// Input integer N
// Output N integers
// Input N integers
// Output some subset of integers from the I/O that halves the total

// }}}

// Prints vector
void printVec(const vector<ll> &v) {
    for (int i = 0; i < v.size(); i++) {
        cout << v[i];
        if (i + 1 < v.size())
            cout << ' ';
    }
    cout << endl;
}

void solve() {

    int N;
    cin >> N;

    int curr_price;
    vll prices;
    F0R(i, N) {
        cin >> curr_price;
        prices.pb(curr_price);
    }
    // printVec(prices);

    int max_served = min(prices.front(), prices.back());
    int score = 0;
    F0R(i, N) {
        if (prices.front() < prices.back()) {
            if (prices.front() >= max_served) {
                max_served = prices.front();
                score++;
            }
            prices.erase(prices.begin());
        } else {
            if (prices.back() >= max_served) {
                max_served = prices.back();
                score++;
            }
            prices.pop_back();
        }
    }
    cout << score << "\n";
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
