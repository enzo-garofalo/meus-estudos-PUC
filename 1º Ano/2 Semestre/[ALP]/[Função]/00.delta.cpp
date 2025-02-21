#include <iostream>
using namespace std;

double Delta(double a, double b, double c){
    double delta = b*b - 4 * a * c;
    return delta;
}

int main(){
    double a, b, c;
    cout << "Digite A:";
    cin >> a;
    cout << "Digite B:";
    cin >> b;
    cout << "Digite C:";
    cin >> c;

    double deltaVal = Delta(a, b, c);
    if (Delta < 0) cout << "X";
    else if (Delta == 0) cout << "X1";
    else  cout << "X1, X2";
}