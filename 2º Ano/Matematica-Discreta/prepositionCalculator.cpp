#include <iostream>
#include <vector>
#include <map>
#include <cmath>

using namespace std;

// Função para avaliar uma expressão lógica simples
bool avaliarExpressao(string expressao, map<char, bool> valores) {
    vector<bool> pilha;
    
    for (char c : expressao) {
        if (c >= 'A' && c <= 'Z') {
            pilha.push_back(valores[c]);
        } else if (c == '¬') {
            bool v = pilha.back(); pilha.pop_back();
            pilha.push_back(!v);
        } else if (c == '∧') {
            bool v1 = pilha.back(); pilha.pop_back();
            bool v2 = pilha.back(); pilha.pop_back();
            pilha.push_back(v1 && v2);
        } else if (c == '∨') {
            bool v1 = pilha.back(); pilha.pop_back();
            bool v2 = pilha.back(); pilha.pop_back();
            pilha.push_back(v1 || v2);
        } else if (c == '→') {
            bool v1 = pilha.back(); pilha.pop_back();
            bool v2 = pilha.back(); pilha.pop_back();
            pilha.push_back(!v2 || v1);
        } else if (c == '↔') {
            bool v1 = pilha.back(); pilha.pop_back();
            bool v2 = pilha.back(); pilha.pop_back();
            pilha.push_back(v1 == v2);
        }
    }
    return pilha.back();
}

// Gerar tabela verdade
void gerarTabelaVerdade(string expressao, vector<char> variaveis) {
    int n = variaveis.size();
    int linhas = pow(2, n);
    
    // Cabeçalho da tabela
    for (char var : variaveis) cout << var << " ";
    cout << "| " << expressao << endl;
    cout << string(n * 2 + expressao.length() + 3, '-') << endl;

    // Gerar todas as combinações de valores de verdade
    for (int i = 0; i < linhas; i++) {
        map<char, bool> valores;
        for (int j = 0; j < n; j++) {
            valores[variaveis[j]] = (i & (1 << (n - j - 1))) != 0;
            cout << valores[variaveis[j]] << " ";
        }
        cout << "| " << avaliarExpressao(expressao, valores) << endl;
    }
}

int main() {
    string expressao = "AB∧C∨C"; // Forma pós-fixa: (A ∧ B) ∨ C
    vector<char> variaveis = {'A', 'B', 'C'};

    gerarTabelaVerdade(expressao, variaveis);
    
    return 0;
}
