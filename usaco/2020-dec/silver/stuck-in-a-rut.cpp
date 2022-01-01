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
// http://www.usaco.org/index.php?page=viewproblem2&cpid=1064

// 1 <= N <= 1000 cows
// Each cow face North or East
// Each Step:
//      Stop of grass patch was eaten
//      Eat current cell, move forward 1 cell
//      If 2 cows overlap, they share and continue
// For each cow, print how many cows they stopped
//      Stopping means causing another to stop

// Example
// In:
// Out:

// }}}

struct cow {
    int i = 0;
    int x;
    int y;
    int blame = 0;
    bool flag = false;
};

int main() {

    // Remove param to input 
    setIO("rut");

    int N;
    cin >> N;

    vector<cow> east_cows;
    vector<cow> north_cows;
    cow curr_cow;
    char dir;

    // Save each cow inputted as "east_cow" or "north_cow"
    for (int i = 0; i < N; i++) {
        cin >> dir >> curr_cow.x >> curr_cow.y;
        curr_cow.i = i;
        if (dir == 'E')
            east_cows.push_back(curr_cow);
        else
            north_cows.push_back(curr_cow);
    }

    // Sort both cows to see what collisions happen first
    sort(begin(east_cows), end(east_cows),
         [](const cow &a, const cow &b) { return a.y < b.y; });
    sort(begin(north_cows), end(north_cows),
         [](const cow &a, const cow &b) { return a.x < b.x; });

    // Simulate
    // If a cow hasn't been flagged yet, check if it will collide
    // If it collides, update the blame and flag the stopped one
    for (cow &a : east_cows) {
        for (cow &b : north_cows) {
            if (!b.flag && !a.flag && a.x < b.x && b.y < a.y) {
                if (b.x - a.x < a.y - b.y) {
                    b.flag = true;
                    a.blame += b.blame + 1;
                } else if (b.x - a.x > a.y - b.y) {
                    a.flag = true;
                    b.blame += a.blame + 1;
                }
            }
        }
    }

    // Move the .blame into one vector to output
    // Not sure why I can't move this above
    // But this is more idiomatic(?)
    vector<int> blame(N, 0);
    for (cow curr : east_cows)
        blame[curr.i] = curr.blame;
    for (cow curr : north_cows)
        blame[curr.i] = curr.blame;

    for (int n : blame)
        cout << n << endl;
}
