#include<iostream>
#include<vector>

using namespace std;

int main(){
    int month, day;
    cin >> month >> day;
    
    vector<vector<int>> gothec = { {1,7}, {3,3}, {5,5}, {7,7}, {9,9}};

    for (vector<int> x : gothec){
        if(month == x[0] && day == x[1]){
            cout << "Yes\n";
            return 0;
        }
    }

    cout << "No\n";
    return 0;
}