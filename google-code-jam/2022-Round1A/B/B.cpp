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

// Input integer N
// Output N integers
// Input N integers
// Output some subset of integers from the I/O that halves the total

// }}}

// Inputs integer, exit if x == -1 (Error)
int inp() {
    int x;
    cin >> x;
    if (x == -1)
        exit(0);
    return x;
}

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

    int N = inp();
    assert(N == 100);

    vll nums;
    F0R(i, N) {
        if (i < 30) {
            nums.pb(1LL << i); // 1, 2, 4, ... to 2^29 or 2^N
        } else {
            nums.pb(1000000000 - i);
        }
    }

    printVec(nums);

    // Input new numbers
    F0R(i, N)
    nums.pb(inp());

    sort(nums.begin() + 30, nums.end());

    ll total = 0;
    foreach (x, nums)
        total += x;

    assert(total % 2 == 0);
    total /= 2;

    vll ans;

    R0F(i, sz(nums)) {
        if (total >= nums[i]) {
            total -= nums[i];
            ans.pb(nums[i]);
        } else {
            break;
        }
    }

    F0R(i, 30) {
        if (total & (1LL << i))
            ans.pb(1LL << i);
    }

    printVec(ans);
}

int T;

int main() {
    setIO("test");

    cin >> T;
    while (T--)
        solve();

    cout.flush();
    return 0;
}
