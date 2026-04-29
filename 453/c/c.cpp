#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
    int n;
    double x = 0.5;
    int l;
    cin >> n;
    int c = 0;
    bool diff;
    double d;
    for(int i = 0; i < n; i++){
        cin >> l;
        if(abs(x - l) < abs(x + l)){
            d = x - l;
            diff = false;
        }else if(abs(x - l) > abs(x + l)){
            d = x + l;
            diff = true;
        }else{
            continue;
        }

        if(diff){//right
            x += l;
            if(x > 0){
                c++;
            }
        }else{//left
            x -= l;
            if(x < 0){
                c++;
            }
        }
    }

    cout << c << endl;
    return 0;
}