// Headers {{{
#include <algorithm>
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

// http://www.usaco.org/index.php?page=viewproblem2&cpid=939

// 10x10 farm
// B = Barn, L = Lake, R = Rock
// Cows can only touch adjacently
// Min number of cows to connect B to L without crossing R

// Rock doesn't matter here UNLESS all on same row or col

// }}}

string row;

int main() {

    setIO("buckets");

    int Bx, By, Lx, Ly, Rx, Ry;

    // Input
    for (int i = 0; i < 10; i++) {
        cin >> row;
        for (int j = 0; j < 10; j++) {
            if (row[j] == 'B') {
                Bx = i;
                By = j;
            } else if (row[j] == 'L') {
                Lx = i;
                Ly = j;
            } else if (row[j] == 'R') {
                Rx = i;
                Ry = j;
            }
        }
    }

    // If all in a row and rock is in between
    if ((Bx == Rx && Rx == Lx) &&
        ((By < Ry && Ry < Ly) || (By > Ry && Ry > Ly))) {
        cout << abs(By - Ly) + 1;
    // If all in a col and rock is in between
    } else if ((By == Ry && Ry == Ly) &&
               ((Bx < Rx && Rx < Lx) || (Bx > Rx && Rx > Lx))) {
        cout << abs(Bx - Lx) + 1;
    // else
    } else {
        cout << abs(Bx - Lx) + abs(By - Ly) - 1;
    }

}
