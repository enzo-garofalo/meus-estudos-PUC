#include <iostream>
using namespace std;

void get_vec(int vec[], int len){
    for(int pos=0; pos<len; pos++) cout << vec[pos] << " _ ";
    cout << "\n\n";
}

int main(){
    int vec[10];
    int len_maior = 0, len_menor = 0;

    for(int i=0; i < 10; i++){
        cout << "Digite a posicao " << i << " Para o Vetorzão: ";
        cin >> vec[i];
        cout << "-------------------------------------" << endl;

        if(vec[i] >= 50) len_maior++;
        if(vec[i] < 50) len_menor++;
    }

    int maior_igual[len_maior];
    int menor[len_menor];
    int pos_maior=0, pos_menor=0;

    for(int i = 0; i< 10; i++){
        if(vec[i] >= 50){
            maior_igual[pos_maior] = vec[i];
            pos_maior++;
        }else{
            menor[pos_menor] = vec[i];
            pos_menor++;
        }
    }
    get_vec(maior_igual, len_maior);
    get_vec(menor, len_menor);
    get_vec(vec, 10);

}