#include <iostream>
using namespace std;

struct produto{
    int cod;
    int qtd;
    float valor_compra;
    float valor_venda;
};

void Maior_lucro()

void Maior_estoque(struct produto prod[]){
    int codigo_maior = prod[0].cod, maior_qtd = prod[0].qtd;

    for(int i = 0; i <= 10; i++){
        if(prod[i].qtd > maior_qtd){
            maior_qtd = prod[i].qtd;
            codigo_maior = prod[i].cod;
        }
    }
    cout << "\n\t\t Produto com maior quantidade\n";
    cout << "\nCódigo do produto: " << codigo_maior;
    cout << "\nQuantidade: " << maior_qtd;
}


int main(){
    cout << "\n==========================\n";
    struct produto prod[10];
    
    for(int i = 0; i <= 10; i++){
        while(true){
            cout << "\nDigite o codigo do produto: ";
            cin >> prod[i].cod;
            if(prod[i].cod > 999 || prod[i].cod < 0){
                cout << "\n\t\tDigite um codigo valido!";
                continue;
            }else{
                break;
            }
        }

        cout << "\n==========================";
        cout << "\nDigite a quantidade em estoque: ";
        cin >> prod[i].qtd;
        cout << "\n==========================";

        cout << "\nDigite o valor de compra: ";
        cin >> prod[i].valor_compra;
        cout << "\n==========================";

        cout << "\nDigite o valor de compra: ";
        cin >> prod[i].valor_venda;
        cout << "\n==========================";
        
    }

}