#include <bits/stdc++.h>
using namespace std;
#define int long long

int entrada[10000000];
int tree[4*10000000];


void build(int no, int l, int r){
    if (l==r){tree[no] = entrada[l];}
    else{
        int mid = (l+r)/2;
        build(2*no,l,mid);
        build(2*no+1,mid+1,r);
        tree[no] = tree[2*no] * tree[2*no+1];
    }
}

void update(int no, int l, int r, int i, int val) {
    if (l==r){tree[no] = val;}
    else {
        int mid = (l+r)/2;
        if (i <= mid) update(2*no,l,mid,i,val);
        else update(2*no+1,mid+1,r,i,val);
        tree[no] = tree[2*no] * tree[2*no+1];
    }
}

int query(int no, int l, int r, int i, int j) {
    if ( r < i || l > j) return 1;
    if (l >= i && r <= j) return tree[no];
    int mid = (l+r)/2;
    int p1 = query(2*no,l,mid,i,j);
    int p2 = query(2*no+1,mid+1,r,i,j);
    return p1 * p2; 
}
signed main(){
    int a,b,c;
    cin >> a >> b >> c;
    if (b-a == c-b) {
        cout << "PA " << (c  + c -b);
    }
    else {
        cout << "PG " << (c * c/b);
    }
    return 0;
}