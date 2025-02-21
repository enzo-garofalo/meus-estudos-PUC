#include <iostream>
using namespace std;


void GetDeterminant(double M[3][3], double *det) {
    *det =  M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
        - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
        + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]);

}

void GetAdj(double M[3][3], double adj[3][3]) {
    adj[0][0] = (M[1][1] * M[2][2] - M[1][2] * M[2][1]);
    adj[0][1] = (M[0][2] * M[2][1] - M[0][1] * M[2][2]);
    adj[0][2] = (M[0][1] * M[1][2] - M[0][2] * M[1][1]);

    adj[1][0] = (M[1][2] * M[2][0] - M[1][0] * M[2][2]);
    adj[1][1] = (M[0][0] * M[2][2] - M[0][2] * M[2][0]);
    adj[1][2] = (M[0][2] * M[1][0] - M[0][0] * M[1][2]);

    adj[2][0] = (M[1][0] * M[2][1] - M[1][1] * M[2][0]);
    adj[2][1] = (M[0][1] * M[2][0] - M[0][0] * M[2][1]);
    adj[2][2] = (M[0][0] * M[1][1] - M[0][1] * M[1][0]);
}

void  Multiply(double M[3][3], double b[], double sol[]){
    
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            sol[i] += M[i][j] * b[j];
        }
    }
}

void GetInv(double M[3][3], double inv[3][3]){
    double *det = 0;
    GetDeterminant(M, det);
    
    double adj[3][3];
    GetAdj(M, adj);
    
    double det_inv = 1.0/(*det);
  
    for(int i = 0; i < 3; i++){
        for(int j = 0; j< 3; j++){
            inv[i][j] =  det_inv * adj[i][j];
        }
    }

}

void GetSolution(double M[3][3], double b[], double sol[]){
    double inv[3][3];
    GetInv(M, inv);
    Multiply(inv, b, sol);
}

int main()
{
    double M[3][3];
    double b[3];
    double sol[3];
    
    cout << "\t\tPreencha a matriz:";
    cout << "\n===================================================";
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            cout << "\nPreencha linha [" << i << "] coluna [" << j << "]: ";
            cin >> M[i][j];
        }
        cout << "\n===================================================";
    }
    
    cout << "\n\t\tPreencha o vetor igualdade:";
    cout << "\n===================================================";
    for(int pos = 0; pos < 3; pos++){
        cout << "\nPreencha posicao [" << pos << "]: ";
        cin >> b[pos];
    }
    cout << "\n===================================================";
    
    GetSolution(M, b, sol);
    char caracter[] = {"X""Y""Z"};
    for(int pos = 0; pos < 3; pos++){
        cout << "\nposicao [" << caracter[pos] << "]: " << sol[pos];
    } 

	return 0;
}