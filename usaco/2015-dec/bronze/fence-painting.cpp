#include <iostream>
#include <fstream>

using namespace std;

// Fence = Number line
// John paints interval [a, b], total of b-a sections
// Bessie accidently paints [c, d]
// Output total amount of fence painted

ofstream fout ("paint.out");
ifstream fin ("paint.in");

int a, b, c, d;

int main() {

    fin >> a >> b >> c >> d;

    // Exclusive ranges
    if (b <= c || a >= d) {
        fout << (b - a) + (d - c);
    // (a,b) surrounds (c,d)
    } else if (a <= c && d <= b) {
        fout << (b - a);
    // (c,d) surrounds (a,b)
    } else if (c <= a && b <= d) {
        fout << (d - c);
    // [  (  ]   )
    } else if (c < b) {
        fout << (b - c);
    // (  [  )   ]
    } else {
        fout << (d - a);
    }

}
