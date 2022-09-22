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

bool isPalindrome(string str)
{
    int sz = str.length();
    F0R(i, sz / 2)
        if (str[i] != str[sz - i - 1])
            return false;
    return true;
}

void solve() {
    int len;
    string palindrome;

    cin >> len >> palindrome;
    F0R(i, len - 1) {
        if (isPalindrome(palindrome.substr(i + 1))) {
            string answer = palindrome.substr(0, i + 1);
            reverse(all(answer));
            cout << answer << endl;
            return;
        }
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
