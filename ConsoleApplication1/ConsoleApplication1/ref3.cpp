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
int main()
{
	// entrada
	int Nl, Nt, sum, instancia;
	sum = 0;
	cin >> Nl;
	vector<int> L1(Nl), Lsoma(Nl);
	for (int i = 0; i < Nl; i++)
	{
		cin >> instancia;
		sum += instancia;
		L1[i] = sum;
	}
	cin >> Nt;
	vector<int> L2(Nt);
	for (int i = 0; i < Nt; i++) {
	cin >> L2[i];
	}

	// processo
	for (int i = 0; i < L2.size(); i++) {
		int p1,p2;
		p1 = 0;
		p2 = L1.size() -1;
		if (L2[i] <= L1[p1]) {cout << 1 << endl;}
		else if (L2[i] > L1[p2-1]) {cout << p2+1 << endl;} // 1 3 | p1 =5 p2 = 7 | 9 11 13
		else{
			while (true) {
				int mid = (p1 + p2) / 2;
				//cout << L2[i] << L1[mid] << endl;
				if (L2[i] == L1[mid]) { cout << mid + 1 << endl; break; }
				else if ((L2[i] > L1[p1]) && (L2[i] <= L1[p1+1])){cout << p1+2 << endl;break;}
				else if (L2[i] > L1[mid]){p1 = mid;}
				else if (L2[i] < L1[mid]){p2 = mid;}
			}
		}
	}
}
