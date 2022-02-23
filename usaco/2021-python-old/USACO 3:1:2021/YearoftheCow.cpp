/*
 ID: dazzlethelightwing
 LANG: CPP
 TASK: Comfortable Cows
*/

#include <bits/stdc++.h>

using namespace std;

int n, k;

int main()
{
    cin.tie(0)->sync_with_stdio(0);

    cin >> n >> k;
    vector<int> years;
    int year_max = 0;
    int year_min = INT_MAX;
    for (int i = 0; i < n; i++)
    {
        int year;
        cin >> year;
        years.push_back(year);

        year_min = min(year, year_min);
        year_max = max(year_max, year);
    }

    int true_start = floor(year_min / 12.0) * 12;
    int true_end = ceil(year_max / 12.0) * 12;

    for (int i = true_start; i <= true_end; i += 12)
    {
        years.push_back(i);
    }
    sort(years.begin(), years.end());
    reverse(years.begin(), years.end());

    int start = years.at(0);
    int total = 0;
    for (int i = 1; i < years.size() - 1; i++)
    {
        if (years.at(i) % 12 == 0)
        {
            if (years.at(i) != years.at(i + 1))
            {
                int j = i + 1;
                int end_natural = years.at(i);
                while (years.at(j) % 12 == 0)
                {
                    j++;
                }

                if (j != i + 1)
                {
                    int year_num = start - end_natural;

                    start = years.at(j - 1);
                    i = j;
                    total += year_num;
                }
            }
        }
        if (i == years.size() - 2)
        {
            total += start - years.at(years.size() - 1);
        }
    }
    cout << total << endl;
}