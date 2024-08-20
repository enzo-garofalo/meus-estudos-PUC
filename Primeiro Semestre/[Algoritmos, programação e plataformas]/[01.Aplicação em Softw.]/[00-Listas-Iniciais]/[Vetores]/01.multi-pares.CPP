#include <iostream>
using namespace std;


int get_n(){
    int n;
    while(true){
        cout << "Digite o valor de N: ";
        cin >> n;
        if(n > 20 || n <= 0){
            cout << "\nDigite um valor valido!\n";
            continue;
        }
        break;
    }
    return n;
}

void set_val(float vec[], int pos){
    cout << "\nDigite a posicao " << pos << " Para o Vetor : ";
    cin >> vec[pos];
}

int main(){

    int n = get_n();
    float x[n];
    float y[n];
    float z[n];
    for(int i = 0; i < n; i++){
        set_val(x, i);
        set_val(y, i);
        cout << "===============================================\n";

        z[i] = x[i]*y[i];
    }
    for(int position = 0; position < n; position++) cout <<"Z"<< position << ": "<< z[position] << endl;

}