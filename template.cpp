#include<bits/stdc++.h>
#define MAX 1000050
#define INF 0x3f3f3f3f
using namespace std;
typedef long long ll;

int n;
struct node{ll x, y;}
points[MAX];
ll Abs(ll x){return x >= 0 ? x : (-x);}
bool cmp(node a, node b){return a.x == b.x ? a.y < b.y : a.x < b.x;}

void test1(int idx){
    ll mx = -INF;
    scanf("%lld%lld", &points[idx].x, &points[idx].y);
    mx = max(mx, points[idx].y);
    sort(points + 1, points + n + 1, cmp);
}

char grid[MAX][MAX];
int dp[MAX][MAX][MAX];

void test2(){
    memset(dp, -1, sizeof dp);
    vector<int> price(MAX, -1), pages(MAX, -1);
    vector<vector<int> > dp(n+1,vector<int>(MAX+1,0));
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int t; scanf("%d", &t);
    while(t--){
        //solve
    }
}