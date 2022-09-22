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
// }}}

int main() {
    setIO();

    int T;
    cin >> T;

    vi nums;
    int inp;
    int even = 0;
    F0R(i, T) {
        cin >> inp;
        even += inp % 2 == 0 ? 1 : -1;
        nums.pb(inp);
    }

    F0R(i, nums.size()) {
        if (even > 0 && nums[i] % 2 == 1)
            cout << i + 1 << endl;
        if (even < 0 && nums[i] % 2 == 0)
            cout << i + 1 << endl;
    }

    return 0;
}

