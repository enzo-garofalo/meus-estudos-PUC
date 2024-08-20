//Lista 1
//Construa utilizando valores aleatórios, as seguintes matrizes: 
// Efetue as operações abaixo usando os 
// comandos apropriados:

A=[1 2 3 4 5; 6 7 8 9 10; 1 2 3 4 5; 6 7 8 9 10;1 2 3 4 5; 6 7 8 9 10; 1 2 3 4 5; 6 7 8 9 10;]
B=[5 4 3 2 1; 7 8 9 4 3; 1 4 2 5 7;]
C=[9 8 3 4 2 3 7 8; 3 4 2 5 7 8 9 1; 3 5 6 7 4 2 4 9; 6 2 3 7 2 9 1 3; 2 4 5 6 1 2 8 9]
D=[1 5 6; 3 5 9; 9 2 4]

printf("A= ")
disp(A)

printf("B= ")
disp(B)

printf("C= ")
disp(C)

printf("D= ")
disp(D)

printf("a) AB^t= ")
disp(A*B')

printf("b) C - A^t = ")
disp(C-A')

printf("c) b^t*D = ")
disp(B'*D)
