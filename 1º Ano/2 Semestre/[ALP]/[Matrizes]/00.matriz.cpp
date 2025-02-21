#include <iostream>
using namespace std;

int main(){
    int a[6][6];
    for(int linha = 0; linha < 6; linha++){
        for(int col = 0; col < 6; col++){
            if(linha==col){
                a[linha][col] = 1;
            }else{
                a[linha][col] = 0;
            }

        }
    }

    for(int i=0; i < 6; i++){
        printf("\n\t\t");
        for(int j = 0; j < 6; j++){
            cout << a[i][j] << " ";
        }
    }

    return 0;
}