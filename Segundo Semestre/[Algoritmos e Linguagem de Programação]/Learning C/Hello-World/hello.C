/* 
A linha #include <stdio.h> diz ao compilador que ele deve incluir o arquivo-cabeçalho stdio.h. 
Neste arquivo existem declarações de funções úteis para entrada e saída de dados
(std = standard, padrão em inglês; io = Input/Output, entrada e saída ==> stdio = Entrada e saída padronizadas). 
Toda vez que você quiser usar uma destas funções deve-se incluir este comando. 
O C possui diversos arquivos-cabeçalhos.
*/
#include <stdio.h>
#include <iostream>

int main()
{
    std::cout << "ola\n";
    printf("Eita mundo bao!");
    return 0;
}