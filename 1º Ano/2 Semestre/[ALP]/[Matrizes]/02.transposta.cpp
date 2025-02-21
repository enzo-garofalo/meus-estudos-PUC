/*  
    Faça um algoritmo que leia uma matriz de inteiros 5x3 e
    construa sua transposta. O programa deverá imprimir as
    duas matrizes, a original e a transposta.
*/
#define i 3
#define j 2
#include <iostream>
using namespace std;

void set_matrix(int M[i][j]){
    float num = 0;
    for(int linha=0; linha<i; linha++){
        cout << "----------------------------------------------------" << endl;
        for(int col=0; col<j; col++){
            cout << "Digite o numero da linha [" << linha+1 << "] coluna [" << col+1 <<"]: ";
            cin >> num;

            M[linha][col] = num;
        }
    }
}

void get_matrix(int matrix[i][j]){
    for(int linha=0; linha<i; linha++){
        printf("\n\t\t");
        for(int col=0; col<j; col++){
            cout << "| " << matrix[linha][col] << " | ";
        }
    }
}

void get_Tmatrix(int matrix[i][j]){
    for(int col=0; col < j; col++){
        printf("\n\t\t");
        for(int linha=0; linha < i; linha++){
            cout << matrix[linha][col] << " | ";
        }
    }
}

int main(){
    int M[i][j];
    set_matrix(M);
    cout << "----------------------------------------------------" << endl;
    printf("\t\tMatriz Original:");
    get_matrix(M);

    cout << "\n----------------------------------------------------" << endl;

    printf("\t\tMatriz Transposta:");
    get_Tmatrix(M);
    cout << "\n----------------------------------------------------" << endl;

    return 0;
}