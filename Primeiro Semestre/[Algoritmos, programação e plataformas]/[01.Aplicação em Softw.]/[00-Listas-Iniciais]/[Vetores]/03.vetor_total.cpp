#include <iostream>
using namespace std;

int get_n(){
    int n;
    while(true){
        cout << "Digite o valor de N: ";
        cin >> n;
        cout << endl;
        if(n > 20 || n <= 0){
            cout << "Digite um valor valido!\n";
            continue;
        }
        break;
    }
    return n;
}

void set_val(int vec[], int n){
    for(int pos = 0; pos < n; pos++){
        cout << "\nDigite a posicao " << pos << " Para o Vetor X: ";
        cin >> vec[pos];
    }
}

void get_vec(int vec[], int n){
    for(int position = 0; position < n; position++) cout <<"X"<< position << ": "<< vec[position] << endl;
}

int main(){
    int soma = 0;
    int n = get_n();
    int x[n];
    set_val(x, n);
    for(int i = 0; i < n; i++){
        soma = soma + x[i];
    }
    get_vec(x, n);
    cout << "Soma: " << soma;
}