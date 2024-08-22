#include <iostream>
using namespace std;

int fatorial(int num){
    if(num == 1){
        return 1;
    }

    return num * fatorial(num-1);
}

int main(){
    int num = 0;
    cout << "Digite num: ";
    cin >> num;

    cout << num << "! = " << fatorial(num) << endl;
    return 0;
}