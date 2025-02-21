#define i 10
#define j 10

#include <iostream>
using namespace std;

void set_board(){
    for(int linha = 0; linha < i; linha){
        for (int col = 0; col < j; col++)
        {
            cout << " ~~ ";
        }
            cout << endl;
        
    }
}

int main(){
    set_board();
    return 0;
}