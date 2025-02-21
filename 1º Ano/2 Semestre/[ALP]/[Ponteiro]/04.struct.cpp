#include <iostream>
using namespace std;

struct Aluno{
    char nome[100];
    int matricula;
    float nota;
};

int menu(){
    cout << "====================================\n";
    cout << "\t\tMenu\n";
    cout << "====================================";
    cout << "1 - Cadastrar Aluno" << endl;
    cout << "2 - Mostrar Alunos" << endl;
    cout << "3 - Buscar Alunos" << endl;
    cout << "4 - Sair" << endl;
    cout << "====================================\n";
    int escolha = 0;
    cin >> escolha;

    return escolha;
}
void cadastrar(){

}

void mostrar(){

}

void buscar(){
    
}

int main(){

    int escolha = menu();

    switch (escolha)
    {
    case 1:
        cadastrar();
    case 2:
        mostrar();
    case 3:
        buscar();
    
    case 4:
        return 0;
    default:
        escolha = menu();
    }



    return 0;
}