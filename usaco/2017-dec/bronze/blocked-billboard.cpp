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

// http://www.usaco.org/index.php?page=viewproblem2&cpid=759

// row 1: x1, y1, x2, y2 of billboard A
// row 2: x1, y1, x2, y2 of billboard B
// row 3: x1, y1, x2, y2 of truck
// Calculate area of the billboards not covered by the truck
// Note: x1 < x2, y1 < y2
// Note: Billboard do not overlap

// }}}

struct Rect {
    int x1, y1, x2, y2;
    int area() { return (y2 - y1) * (x2 - x1); };
};

int intersect(Rect p, Rect q) {
    int xOverlap = max(0, min(p.x2, q.x2) - max(p.x1, q.x1));
    int yOverlap = max(0, min(p.y2, q.y2) - max(p.y1, q.y1));
    return xOverlap * yOverlap;
}

int main() {
    setIO("billboard");

    Rect board1, board2, truck;
    cin >> board1.x1 >> board1.y1 >> board1.x2 >> board1.y2;
    cin >> board2.x1 >> board2.y1 >> board2.x2 >> board2.y2;
    cin >> truck.x1 >> truck.y1 >> truck.x2 >> truck.y2;

    cout << board1.area() + board2.area() - intersect(board1, truck) -
                intersect(board2, truck);
}
