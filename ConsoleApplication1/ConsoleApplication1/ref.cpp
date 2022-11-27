#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
#include <set>
#include <stack>
#include <cmath>
#include <queue>
#include <map>


using namespace std;
//ios_base::sync_with_stdio(false); cin.tie(NULL);
int main()
{
	int p1, p2, longest, Llength, Alength, loops;
	longest = Llength = Alength = 0;
	cin >> loops;
	p1 = p2 = loops - 1;
	vector<int> v(loops);
	for (size_t i = 0; i < loops; i++) {
		cin >> v[i];
		if (v[p1] == v[p2]) {
			p1 -= 1;
			Alength += 1;
		}
		else {
			p2 = p1;
			longest = max(longest, min(Alength, Llength));
			Llength = Alength;
			Alength = 0;
		}
	}
	longest = max(longest, min(Alength, Llength));
	cout << longest * 2 << endl;
	return 0;
}
