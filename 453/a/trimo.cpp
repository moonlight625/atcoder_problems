#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
    int n;
    string s;
    cin >> n >> s;

    char x = s[0];
    int j = 0;
    while(s[j] == 'o'){
        j++;
    }

    for (int i = j; i < s.size(); i++)
    {
        cout << s[i];
    }
    cout << endl;
    return 0;
    
}