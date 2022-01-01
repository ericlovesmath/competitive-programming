#include <iostream>

using namespace std;

// Start with n
// If n is even, divide it by 2
// If n is odd, triple it and add 1
// Stop when n is 1

long long n;

int main() {

    cin >> n;

    while (n != 1) {
        cout << n << ' ';
        if (n % 2 == 0) {
            n /= 2;
        } else {
            n = 3 * n + 1;
        }
    }

    cout << n << endl;

}
