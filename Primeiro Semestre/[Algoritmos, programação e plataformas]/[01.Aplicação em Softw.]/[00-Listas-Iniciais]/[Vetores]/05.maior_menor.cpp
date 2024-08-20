/*Ler um vetor de inteiros 10 posições. 
Escreva a seguir o valor e a posição maior e menor dos elemento lidos*/
#include <iostream>
using namespace std;

void set_val(int vec[], int len){
    for(int pos = 0; pos < len; pos++){
        cout << "Digite a posicao " << pos << " Para o Vetor X: ";
        cin >> vec[pos];
        cout << "-------------------------------------" << endl;
    }
}

void max_min(int vec[], int len, int &max, int &min, int &iMax, int &iMin) {
    max = vec[0];
    min = vec[0];
    iMax = 0;
    iMin = 0;

    for (int i = 1; i < len; i++) {
        if (vec[i] > max) {
            max = vec[i];
            iMax = i;
        }
        if (vec[i] < min) {
            min = vec[i];
            iMin = i;
        }
    }
}

int main() {
    int len = 10;
    int vec[len];
    set_val(vec, len);
    
    int max, min, iMax, iMin;
    max_min(vec, len, max, min, iMax, iMin);
    
    cout << "Maior Valor: " << max << " Posicao: " << iMax << endl;
    cout << "Menor Valor: " << min << "  Posicao: " << iMin << endl;

    return 0;
}