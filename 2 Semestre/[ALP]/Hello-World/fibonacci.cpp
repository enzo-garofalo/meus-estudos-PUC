#include <iostream>
using namespace std;

void fibonacci(int num){
    int ult = 1;
    int penult = 0;
    int temp;
    cout << penult << endl << ult << endl;
    for(int i = 0; i < num; i++){
        cout << (ult+penult) << endl;

        temp = penult;
        penult = ult;
        ult += temp;
    }
}

int main(){
    int num = 10;
    cout << "Exibir quantos termos: ";
    cin >> num;

    fibonacci(num);
    
    return 0;
}