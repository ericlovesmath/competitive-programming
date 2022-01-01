// Headers {{{
#include <algorithm>
#include <array>
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

// http://www.usaco.org/index.php?page=viewproblem2&cpid=761

// Bessie, Elsie, and Mildred each produce 7 gal milk per day
// Periodic measurements taken over 100 days
// On day X, cow Y fluctuates output by Z
// He displays the highest output cows everyday
// How often does he need to change?

// }}}

int main() {

    setIO("measurement");

    vector<array<int, 3>> log;

    int N;
    cin >> N;
    log.reserve(N);
    int day, cow_id;
    string cow_str, change;

    // Parse input
    while (N--) {
        cin >> day >> cow_str >> change;
        if (cow_str[0] == 'B')
            cow_id = 0;
        else if (cow_str[0] == 'E')
            cow_id = 1;
        else
            cow_id = 2;

        log.push_back({day, cow_id, stoi(change)});
    }

    // Sort the log
    sort(begin(log), end(log));

    int currmax = 7;
    array<int, 3> cow = {7, 7, 7};
    array<bool, 3> display = {true, true, true};
    int count = 0;

    for (array<int, 3> entry : log) {

        array<bool, 3> display_copy = display;

        // Update currmax, display
        cow[entry[1]] += entry[2];
        currmax = *max_element(begin(cow), end(cow));

        display[0] = (cow[0] == currmax);
        display[1] = (cow[1] == currmax);
        display[2] = (cow[2] == currmax);

        // Check if display updated
        if (display != display_copy)
            count++;
    }

    cout << count;
}
