#include <bits/stdc++.h>
#include <set>
using namespace std;
#define endl '\n'
#define int long long

set<int> s;

int kmex(int k){
    int ki = k;
    int i = 1;
    while (s.find(ki) != s.end()) {
        i++;
        ki = k * i;
    }
    return ki;
}
signed main(){
    int t;
    cin >> t;
    while(t--){
        char o;
        int k;
        cin >> o >> k;
        if(o == '+'){
            s.insert(k);
        }
        else if(o == '-'){
            s.erase(k);
        }
        else{
            cout << kmex(k) << endl;
        }
    }
    return 0;
}