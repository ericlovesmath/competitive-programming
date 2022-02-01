// Headers {{{
#include <algorithm>
#include <array>
#include <iostream>
#include <iterator>
#include <map>
#include <math.h>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;
#define endl '\n'

void setIO(string name = "") { ios_base::sync_with_stdio(0);
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

// Vector
template <typename T> ostream &operator<<(ostream &os, const vector<T> &v) {
    os << "[";
    string sep = "";
    for (auto e : v)
        os << sep << e, sep = ", ";
    return os << "]";
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

// http://www.usaco.org/index.php?page=viewproblem&cpid=1171

// N <= 3e5 cows, heights 1 to N, denoted by h_i
// Two cows i and j are chosen
//      They can only play frisbee if all cows in between are shorter than both
//      of them

// Compute: Sum of distances between all pairs i < j that can throw a frisbee
//      Distance: j - i + 1
// }}}

int main() {

    setIO("frisbee");

    int N;
    cin >> N;

    vector<int> heights;
    heights.reserve(N);

    int input;
    for (int i = 0; i < N; i++) {
        cin >> input;
        heights.push_back(input);
    }

    long long answer = 0;
    stack<int> stack;

    // Mono stack time
    for (int i = 0; i < N; ++i) {

        while (!stack.empty() && heights[i] > heights[stack.top()]) {
            int j = stack.top();
            stack.pop();
            if (i == j + 1) {
                continue;
            }
            answer += (i - j + 1);
        }

        // Test for Adjacency
        if (!stack.empty() && stack.top() != i - 1) {
            answer += i + 1 - stack.top();
        }

        // dbg(answer, i);
        stack.push(i);
    }

    cout << answer + 2 * N - 2;
}
