/*  
    Elabore um programa que leia uma matriz de reais 10x10 e
    determine:
        • A soma da linha 4.
        • O menor elemento da coluna 5.
        • O maior elemento da diagonal principal.
*/
#define i 4
#define j 4
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

int main(){
    int m[i][j];
    set_matrix(m);
    cout << "----------------------------------------------------" << endl;
    printf("\t\tMatriz Original:");
    get_matrix(m);
    cout << "\n----------------------------------------------------" << endl;


    int soma = 0;
    int menor = m[0][5];
    int maior = m[0][0];

    for(int linha = 0; linha < i; linha++){
        for(int col =0; col< j; col++){
            if(linha == 3) 
            soma = soma + m[linha][col];

            if(col == 4 && m[linha][col] < menor) 
            menor = m[linha][col];

            if(linha == col && m[linha][col] > maior) 
            maior = m[linha][col];
        }
    }
    cout << "Soma da linha 4: " << soma << endl;
    cout << "O menor elemento da coluna 5: " << menor << endl;
    cout << "O maior elemento da diagonal principal: " << maior << endl;

    return 0;
}