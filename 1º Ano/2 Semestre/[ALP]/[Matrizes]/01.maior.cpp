/*  
    Faça um algoritmo que leia uma matriz M 5x5 de números reias. 
    O programa deve determinar o maior número da
    matriz e a sua posição (linha, coluna).
*/

#define N 5
#include <iostream>
using namespace std;

void set_matrix(float M[N][N]){
    float num = 0;
    for(int i=0; i<N; i++){
        cout << "----------------------------------------------------" << endl;
        for(int j=0; j<N; j++){
            cout << "Digite o numero da linha [" << i+1 << "] coluna [" << j+1 <<"]: ";
            cin >> num;

            M[i][j] = num;
        }
    }
}

int main(){
    float M[N][N];
    float maior = M[0][0];
    int iMaior, jMaior = 0;
    set_matrix(M);

    for(int i=0; i < N; i++){
        printf("\n\t\t");
        for(int j = 0; j < N; j++){
            cout << M[i][j] << " | ";
            if(M[i][j] > maior){
                maior = M[i][j];
                iMaior = i;
                jMaior = j;
            }
        }
    }
    cout << "\nO maior numero eh: " << maior;
    cout << "\nLinha: " << iMaior+1;
    cout << "\nColuna: " << jMaior+1;

    return 0;
}