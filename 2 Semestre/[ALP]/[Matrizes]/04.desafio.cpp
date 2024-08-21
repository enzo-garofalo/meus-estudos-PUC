#define i 2
#define j 3

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

void set_vec(int vec[]){
    cout << "----------------------------------------------------" << endl;
    printf("\n\t\tPreencha o vetor\n");
    for(int index = 0; index < j; index++){
        cout << "Digite o numero para a posicao [" << index << "]: ";
        cin >> vec[index];
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

void get_vec(int vec[]){
    for(int pos = 0; pos < i; pos++){
        cout << " | " << vec[pos] << " | ";
    }
}


int main(){
    int m[i][j];
    int v[j];

    set_matrix(m);
    set_vec(v);


    int pi[i];
    for(int linha = 0; linha < i; linha++){
        int soma = 0;
        for(int col = 0; col < j; col++){
            soma += m[linha][col] * v[col];
        }
        pi[linha] = soma;
    }

    cout << "\n----------------------------------------------------" << endl;
    printf("\tMatriz Original:");
    get_matrix(m);
    cout << "\n----------------------------------------------------" << endl;
    printf("\n\tVetor V: ");
    get_vec(v);
    cout << "\n----------------------------------------------------" << endl;
    printf("\n\tVetor pi:");
    get_vec(pi);
    cout << "\n----------------------------------------------------" << endl;


    return 0;
}