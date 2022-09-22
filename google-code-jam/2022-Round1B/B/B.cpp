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

// Problem Statement {{{

// Set pressure to x pascals
// Two buttons: increase/decrease target pressure by 1 pascal
//

// }}}

// Prints vector
void printVec(const vi &v) {
    for (int i = 0; i < v.size(); i++) {
        cout << v[i];
        if (i + 1 < v.size())
            cout << ' ';
    }
    cout << endl;
}

void solve() {

    int N, P; // # of people, # of pressures
    
    cin >> N >> P;

    vector<pi> pressures;
    pi customer;
    int curr;
    F0R(i, N) {
        F0R(i, P) {
            cin >> curr;
            if (i == 0) {
                customer.first = curr;
                customer.second = curr;
            }
            if (curr < customer.first)
                customer.first = curr;
            if (curr > customer.second)
                customer.second = curr;
        }
        pressures.pb(customer);
    }

    // TEST MIN-MAX-MIN and MAX-MIN-MAX orders

    ll min_ans = INT_MAX;
    ll curr_ans;
    ll curr_pos;

    F0R(n, pow(2, N)) {
        curr_ans = 0;
        curr_pos = 0;
        F0R(i, N) {
            int curr_bit = (n & ( 1 << i )) >> i;
            if (curr_bit == 0) {
                curr_ans += abs(curr_pos - (pressures[i].first));
                curr_pos = pressures[i].first;
            } else {
                curr_ans += abs(curr_pos - (pressures[i].second));
                curr_pos = pressures[i].second;
            }
        }
        cout << curr_ans << endl;
        if (curr_ans < min_ans)
            min_ans = curr_ans;
    }

    cout << min_ans << endl;
    cout << abs(10 - 30) << endl;

}

int T;

int main() {
    setIO("test");

    cin >> T;
    FOR(i, 1, T+1) {
        cout << "Case #" << i << ": ";
        solve();
    }

    return 0;
}
