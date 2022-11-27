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
    int totalCases;
    cin >> totalCases;
    for (int i = 0; i < totalCases; i++) {
        string mapa;
        string String = "R";
        int Tam,Pos;
        Tam = Pos = 0;
        cin >> mapa;
        String.append(mapa);
        String.append("R");
        for (int j = 0; j < String.length(); j++) {
            if (String[j] == 'R') {
                Tam = max(Tam, j - Pos);
                Pos = j;
            }
        }
        cout << Tam << endl;
    }
}
