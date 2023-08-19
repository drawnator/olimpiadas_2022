#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define endl "\n"

set<pair<ll,ll>> p;

ll find(pair<ll,ll> p1, pair<ll,ll> p2, pair<ll,ll> p3){
    pair<ll,ll> np1;
    np1.first = p1.first + (p2.first-p3.first);
    np1.second = p1.second + (p2.second-p3.second);

    if(p.find(np1) != p.end()){return 1;}

    pair<ll,ll> np2;
    np2.first = p1.first + (p3.first-p2.first);
    np2.second = p1.second + (p3.second-p2.second);

    if(p.find(np2) != p.end()){return 1;}

    pair<ll,ll> np3;
    np3.first = p3.first + (p2.first-p1.first);
    np3.second = p3.second + (p2.second-p1.second);

    if(p.find(np3) != p.end()){return 1;}

    return 0;
}

int main() {
    vector<pair<ll,ll>> points;
    ll n; cin >> n;

    for(int i = 0; i < n; i++){
        ll x, y;
        cin >> x >> y;
        p.insert(make_pair(x,y));
        points.emplace_back(make_pair(x,y));
    }

    ll r; r = 0;

    for(int j = 0; j < n; j++){
        for(int k = j + 1; k < n; k++){
            for(int l = k + 1; l < n; l++){
                r += find(points[j],points[k],points[l]);
            }
        }
    }

    cout << r / 4 << endl;

    return 0;
}