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
#include <unordered_map>
#include <unordered_set>
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

// Set
template <typename A> ostream &operator<<(ostream &os, const set<A> &m) {
    os << "{";
    string sep = "";
    for (auto e : m)
        os << sep << e, sep = ", ";
    return os << "}";
}
template <typename A>
ostream &operator<<(ostream &os, const unordered_set<A> &m) {
    os << "{";
    string sep = "";
    for (auto e : m)
        os << sep << e, sep = ", ";
    return os << "}";
}
template <typename A> ostream &operator<<(ostream &os, const multiset<A> &m) {
    os << "{";
    string sep = "";
    for (auto e : m)
        os << sep << e, sep = ", ";
    return os << "}";
}

// Map
template <typename A, typename B>
ostream &operator<<(ostream &os, const map<A, B> &m) {
    os << "{";
    string sep = "";
    for (auto e : m)
        os << sep << e.first << ": " << e.second, sep = ", ";
    return os << "}";
}
template <typename A, typename B>
ostream &operator<<(ostream &os, const unordered_map<A, B> &m) {
    os << "{";
    string sep = "";
    for (auto e : m)
        os << sep << e.first << ": " << e.second, sep = ", ";
    return os << "}";
}

// Array
template <typename T, size_t L>
ostream &operator<<(ostream &os, const array<T, L> &v) {
    os << "[";
    string sep = "";
    for (int i = 0; i < L; ++i)
        os << sep << v[i], sep = ", ";
    return os << "]";
}

// Pair
template <typename A, typename B>
ostream &operator<<(ostream &os, const pair<A, B> &p) {
    os << '(' << p.first << ", " << p.second << ')';
    return os;
}

// Vector
template <typename T> ostream &operator<<(ostream &os, const vector<T> &v) {
    os << "[";
    string sep = "";
    for (auto e : v)
        os << sep << e, sep = ", ";
    return os << "]";
}
// Tuple
// Source: https://stackoverflow.com/a/31116392/12128483
template <typename Type, unsigned N, unsigned Last> struct TuplePrinter {
    static void print(ostream &out, const Type &value) {
        out << get<N>(value) << ", ";
        TuplePrinter<Type, N + 1, Last>::print(out, value);
    }
};
template <typename Type, unsigned N> struct TuplePrinter<Type, N, N> {
    static void print(ostream &out, const Type &value) { out << get<N>(value); }
};
template <typename... Types>
ostream &operator<<(ostream &out, const tuple<Types...> &value) {
    out << '(';
    TuplePrinter<tuple<Types...>, 0, sizeof...(Types) - 1>::print(out, value);
    return out << ')';
}

void dbg() { cerr << endl; }
template <typename Head, typename... Tail> void dbg(Head H, Tail... T) {
    cerr << ' ' << H;
    dbg(T...);
}
// }}}

// Problem Statement {{{

// http://www.usaco.org/index.php?page=viewproblem&cpid=1172

// Cow eats a box of cereal per meal
// Shipment with 2 <= M <= 1e5 types of cereal, one of each
// Each of the 1 <= N <= 1e5 cows has a first and second pref
//
// Selection process for cows
//      1. Take favorite if exists
//      2. If not, take second favorite if exists
//      3. If not, Be sad and leave

// Find min number of cows that will be hungry

// Input: N, M
// }}}

vector<pair<int, int>> cows;
vector<int> food;

bool fill(int cow, int cereal) {
    if (food[cereal] < 0) {
        food[cereal] = cow;
        return true;
    } else {
        int nextcow = food[cereal];
        if (nextcow < cow && cows[nextcow].first == cereal) {
            if (fill(nextcow, cows[nextcow].second)) {
                food[cereal] = cow;
                return true;
            }
        }
    }
    return false;
}

int main() {

    setIO("cereal2");

    int N, M;
    cin >> N >> M;

    cows.reserve(N);

    pair<int, int> choices;
    for (int i = 0; i < N; i++) {
        cin >> choices.first >> choices.second;
        cows.push_back(choices);
    }

    food.reserve(M + 1);
    for (int i = 0; i < M + 1; i++) {
        food.push_back(-1);
    }

    // dbg(N, M);
    // dbg(cows);
    // dbg(s);

    vector<int> head, tail;
    int answer = 0;
    int a, b;

    for (int i = 0; i < N; i++) {
        a = cows[i].first;
        b = cows[i].second;
        if (fill(i, a)) {
            head.push_back(i);
        } else {
            tail.push_back(i);
            if (food[b] < 0) {
                food[b] = i;
            } else {
                answer++;
            }
        }
    }

    // dbg(answer);
    cout << answer << endl;
    for (int i = head.size() - 1; i >= 0; i--) {
        cout << head[i] + 1 << endl;
    }
    for (int i = 0; i < tail.size(); i++) {
        cout << tail[i] + 1 << endl;
    }
}
