// Headers {{{
#include <algorithm>
#include <climits>
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

// N modules indexed 1 to N with F (fun value) assigned
// Each module points at a lower index or nothing
// If module is pointed by nothing, it is an *initiator*
// Can trigger initiators to cause chain reaction
// Chain Reaction's max fun = fun experienced
// Can't trigger same node twice
// What order to trigger to maximize total fun?

// Directed Graph maximization gang

// }}}

int T, N;
int new_fun, new_pointer;
vector<int> funs;
vector<int> points; // If 0, points to abyss
vector<int> in_deg;

void solve() {

    cin >> T;

    for (int t = 0; t < T; ++t) {

        cout << "Case #" << t + 1 << ": ";
        cin >> N;

        // We do a little shifting here (+1 for simplicity)
        funs.clear();
        funs.push_back(0);
        for (int i = 0; i < N; ++i) {
            cin >> new_fun;
            funs.push_back(new_fun);
        }
        vector<int> in_deg(N + 1, 0);
        points.clear();
        points.push_back(0);
        for (int i = 0; i < N; ++i) {
            cin >> new_pointer;
            points.push_back(new_pointer);
            in_deg[new_pointer]++;
        }

        long long max_fun = 0; // Assuming long long might be needed?
        queue<pair<int, int>> queue;
        for (int i = 1; i <= N; ++i) {
            if (in_deg[i] == 0) {
                queue.push(make_pair(i, funs[i]));
            }
        }

        vector<int> min_fun(N + 1, INT_MAX);

        while (!queue.empty()) {
            int next = points[queue.front().first];
            int fun = queue.front().second;

            queue.pop();

            if (next == 0) {
                max_fun += fun;
            } else {
                in_deg[next]--;

                if (min_fun[next] == INT_MAX)
                    min_fun[next] = fun;
                else {
                    max_fun += max(fun, min_fun[next]);
                    min_fun[next] = min(min_fun[next], fun);
                }

                if (in_deg[next] == 0) {
                    queue.push(make_pair(next, max(min_fun[next], funs[next])));
                }
            }
        }

        cout << max_fun << endl;
    }
}

int main() {
    setIO("test");
    solve();
}
