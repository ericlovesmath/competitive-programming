#define FOR(i, a, b) for(int i = (a); i < (b); i++)
#define FORE(i, a, b) for(int i = (a); i <= (b); i++)
#define F0R(i, a) for(int i = 0; i < (a); i++)
#define trav(a, x) for (auto& a : x)

using arr = array;
using ll = long long;
using str = string;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
using vi = vector<int>;
const int MOD = 1e9 + 7;
const int MAXN = 1e5;
// const + using > define

int N; cin >> N;
vector<int> x(N), y(N);
for (int& t: x) cin >> t;
for (int& t: y) cin >> t;

