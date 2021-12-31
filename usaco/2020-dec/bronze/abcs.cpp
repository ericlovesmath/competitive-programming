// Headers {{{
#include <iostream>
#include <algorithm>
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
    cin.tie(0)->sync_with_stdio(0);
    if (name.size()) {
        freopen((name + ".in").c_str(), "r", stdin);
        freopen((name + ".out").c_str(), "w", stdout);
    }
}
// }}}

// Problem Statement {{{

// Elsie has integers A <= B <= C
// Input: A, B, C, A+B, B+C, C+A, and A+B+C in some order
// All given numbers are [1, 1E9], not necessarily distinct
// Output: A, B, C

// Example
// In: 2 2 11 4 9 7 9
// Out: 2 2 7

// }}}

int main() {

    setIO();

    int arr[7];
    for (int i = 0; i < 7; i++) {
        cin >> arr[i];
    }

    sort(arr, arr + 7);
    cout << arr[0] << ' ' << arr[1] << ' ' << arr[6] - arr[1] - arr[0];
}
