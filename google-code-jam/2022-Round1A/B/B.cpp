// Headers {{{
#include <algorithm>
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
int N;

bool subsetSum(int nums[], int n, int left_sum[], int A[]) {

    if (n < 0) {
        return false;
    }

    if (left_sum[0] == 0 && left_sum[1] == 0) {
        return true;
    }

    bool result = false;

    for (int i = 0; i < 2; i++) {
        if (!result && (left_sum[i] - nums[n]) >= 0) {
            A[n] = i + 1;
            left_sum[i] = left_sum[i] - nums[n];
            result = subsetSum(nums, n - 1, left_sum, A);
            left_sum[i] = left_sum[i] + nums[n];
        }
    }

    return result;
}

void solve() {

    cin >> N;
    int nums[2 * N];

    for (int i = 0; i < N; ++i) {
        nums[i] = i + 1;
        cout << i + 1 << " ";
    }
    for (int i = N; i < 2 * N; ++i) {
        cin >> nums[i];
    }

    cout << endl;

    int sum = accumulate(nums, nums + 2 * N, 0);

    int A[2 * N];
    int left_sum[2];

    for (int i = 0; i < 2; i++) {
        left_sum[i] = sum / 2;
    }

    subsetSum(nums, 2 * N - 1, left_sum, A);

    for (int i = 0; i < 2 * N; i++) {
        if (A[i] == 1) {
            cout << nums[i] << " ";
        }
    }

    cout << endl;
}

int main() {

    setIO("test");
    cin >> T;
    for (int t = 0; t < T; ++t) {
        solve();
    }

}
