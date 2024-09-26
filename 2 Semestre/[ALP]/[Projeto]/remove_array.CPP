#include <iostream>
using namespace std;

void remocaoLivros(struct livros vec[]){
    int id = 0;
    cout << "===========================================";
    cout << "\nDigite o id do livro que deseja remover: ";
    cin >> id;

    for(int i = 0; i < 100; i++){
        
    }
}

void remove(int pos, int *size, int vec[]){
    int elemento = vec[pos];
    for(int i = pos; i < (*size); i++){
        vec[i] = vec[i+1];
    }
    (*size)--;
}

void get_vec(int vec[], int *size){
    for(int i = 0; i < *size; i++)
        cout << "\nPosicao [" << i << "]: " << vec[i];
    
}

int main(){
    int vec[5] = {1, 2, 3, 45, 65};
    int elemento_remover = 0;
    int *size = new int;
    *size = 5;
    
    get_vec(vec, size);

    cout << "\nDigite um valor para remover: ";
    cin >> elemento_remover;
    bool flag = false;
    for(int i = 0; i < 5; i++){
        if (vec[i] == elemento_remover){
            cout << "\n\tElemento encontrado";
            flag = true;
            remove(i, size, vec);
        }
    } 

    if(!flag){
        int resposta = 0;
        cout << "\tElemento nao encontrado";
        cout << "\nDeseja tentar novamente?\n1 - Sim | 2 - Nao\n";
        cin >> resposta;
    
    }
    

    get_vec(vec, size);
    

        
    return 0;
}