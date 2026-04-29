#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
    int n, diff, a0, a1;
    cin >> n >> diff >> a0;
    bool changed = true;
    cout << '0' << a0 << endl;
    for (int i = 1; i < n; i++)
    {
        changed = false;
        cin >> a1;
        if(abs(a0 - a1) >= diff){
            a0 = a1;
            changed = true;
        }

        if(changed){
            cout << i << a0 << endl;
        }
    }
    return 0;
    
}