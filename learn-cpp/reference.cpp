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

#define LOG(x) cout << x << endl

typedef pair<int, int> pii;
typedef long long ll;

const int MAXN = 1e5 + 5;

enum ECarTypes { Sedan, Hatchback, Wagon };

ECarTypes GetPreferredCarType() { return ECarTypes::Hatchback; }

struct wpoint {
    int x;
    int y;
    int w;
};

int multiply(int a, int b) { return a * b; }

int main() {

    // Really Rough Overview
    // Codeforces cries

    wpoint p1 = {0, 1, 5};
    cout << p1.x << p1.y << p1.w << endl;

    int n = multiply(5, 10);
    double d;
    long x;
    long long y;
    vector<int> v = {7, 5, 3, 2};
    v.push_back(1);
    sort(v.begin(), v.end());
    for (int i : v) {
        cout << i;
    }

    map<int, int> m;
    m[0] = 1;
    cout << max(1, 2) << min(1, 2) << abs(-1);
    for (int i = 1; i < 10; i++) {
        cout << ' ';
    }
    if (true) {
    } else if (false) {
    } else {
    };

    int a[5];

    // IO
    int myInt;
    cout << "Enter your favorite number: ";
    cin >> myInt;
    cout << "Your favorite number is " << myInt << endl;

    // Strings
    string myString = "Hello";
    cout << myString + " You";
    myString.append(" Dog"); // Mutable Strings

    // References (Pointers that can't be reassigned)
    string foo = "I am foo";
    string bar = "I am bar";

    string &fooRef = foo; // This creates a reference to foo.
    fooRef += ". Hi!";    // Modifies foo through the reference
    cout << fooRef;       // Prints "I am foo. Hi!"

    //// Vector (Dynamic Array)
    string val;
    vector<string> my_vector;
    cin >> val;
    my_vector.push_back(val);
    my_vector.push_back(val);

    // To iterate through a vector we have 2 choices:
    for (int i = 0; i < my_vector.size(); i++) {
        cout << my_vector[i] << endl;
    }
    for (vector<int>::iterator it = v.begin(); it != v.end(); ++it) {
        cout << *it << " ";
    }

    v.push_back(2); // [2]
    v.push_back(3); // [2, 3]
    v.push_back(7); // [2, 3, 7]
    v.push_back(5); // [2, 3, 7, 5]
    v[1] = 4; // sets element at index 1 to 4 -> [2, 4, 7, 5]
    v.erase(v.begin() + 1); // removes element at index 1 -> [2, 7, 5]
    // this remove method is O(n); to be avoided
    v.push_back(8); // [2, 7, 5, 8]
    v.erase(v.end() - 1); // [2, 7, 5]
    // here, we remove the element from the end of the list; this is O(1).
    v.push_back(4); // [2, 7, 5, 4]
    v.push_back(4); // [2, 7, 5, 4, 4]
    v.push_back(9); // [2, 7, 5, 4, 4, 9]
    cout << v[2]; // 5
    v.erase(v.begin(), v.begin() + 3); // [4, 4, 9]

    // this erases the first three elements; O(n)

    //// Set (Ordered Set)

    set<int> ST;   // Will initialize the set of int data type
    ST.insert(30); // Will insert the value 30 in set ST
    ST.insert(10); // Will insert the value 10 in set ST
    ST.insert(20); // Will insert the value 20 in set ST
    ST.insert(30); // Will insert the value 30 in set ST
    // Now elements of sets are as follows
    //  10 20 30

    // To erase an element
    ST.erase(20); // Will erase element with value 20
    // Set ST: 10 30
    // To iterate through Set we use iterators
    set<int>::iterator it2;
    for (it2 = ST.begin(); it2 != ST.end(); it2++) {
        cout << *it2 << endl;
    }
    // Output:
    // 10
    // 30

    // To clear the complete container we use Container_name.clear()
    ST.clear();
    cout << ST.size(); // will print the size of set ST
    // Output: 0

    // NOTE: for duplicate elements we can use multiset
    // NOTE: For hash sets, use unordered_set. They are more efficient but
    // do not preserve order. unordered_set is available since C++11

    //// Maps (Ordered Map)

    map<char, int>
        mymap; // Will initialize the map with key as char and value as int

    mymap.insert(pair<char, int>('A', 1));
    // Will insert value 1 for key A
    mymap.insert(pair<char, int>('Z', 26));
    // Will insert value 26 for key Z

    // To iterate
    map<char, int>::iterator it3;
    for (it3 = mymap.begin(); it3 != mymap.end(); ++it3)
        std::cout << it3->first << "->" << it3->second << endl;
    // Output:
    // A->1
    // Z->26

    // To find the value corresponding to a key
    it3 = mymap.find('Z');
    cout << it3->second;

    // Output: 26

    // NOTE: For hash maps, use unordered_map. They are more efficient but do
    // not preserve order. unordered_map is available since C++11.

    // Containers with object keys of non-primitive values (custom classes)
    // require compare function in the object itself or as a function pointer.
    // Primitives have default comparators, but you can override it.

    //// Range

    // You can use a range for loop to iterate over a container
    int arr[] = {1, 10, 3};

    for (int elem : arr) {
        cout << elem << endl;
    }

    //// Tuple

    auto first = make_tuple(10, 'A');
    const int maxN = 1e9;
    const int maxL = 15;
    auto second = make_tuple(maxN, maxL);

    // Printing elements of 'first' tuple
    cout << get<0>(first) << " " << get<1>(first) << '\n'; // prints : 10 A

    // Printing elements of 'second' tuple
    cout << get<0>(second) << " " << get<1>(second)
         << '\n'; // prints: 1000000000 15

    // Unpacking tuple into variables

    int first_int;
    char first_char;
    tie(first_int, first_char) = first;
    cout << first_int << " " << first_char << '\n'; // prints : 10 A

    tuple<int, char, double> third(11, 'A', 3.14141);
    // tuple_size returns number of elements in a tuple (as a constexpr)

    cout << tuple_size<decltype(third)>::value << '\n'; // prints: 3

    // tuple_cat concatenates the elements of all the tuples in the same order.
    auto concatenated_tuple = tuple_cat(first, second, third);
    // concatenated_tuple becomes = (10, 'A', 1e9, 15, 11, 'A', 3.14141)
    cout << get<0>(concatenated_tuple) << '\n'; // prints: 10
    cout << get<3>(concatenated_tuple) << '\n'; // prints: 15
    cout << get<5>(concatenated_tuple) << '\n'; // prints: 'A'

    // Pair
    
    pair<string, int> myPair1 = make_pair("Testing", 123);
	cout << myPair1.first << " " << myPair1.second << endl;
	myPair1.first = "It is possible to edit pairs after declaring them";
	cout << myPair1.first << " " << myPair1.second << endl;
	pair<string, string> myPair2 = {"Testing", "curly braces"};
	cout << myPair2.first << " " << myPair2.second << endl;
}
