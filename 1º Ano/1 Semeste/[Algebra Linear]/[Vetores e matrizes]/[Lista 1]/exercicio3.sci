//Lista 1
//Exercício 3
//Usando as matrizes do exercício 2, obtenha:
A=[1 2 3 4 5; 6 7 8 9 10; 1 2 3 4 5; 6 7 8 9 10;1 2 3 4 5; 6 7 8 9 10; 1 2 3 4 5; 6 7 8 9 10;]
B=[5 4 3 2 1; 7 8 9 4 3; 1 4 2 5 7;]
C=[9 8 3 4 2 3 7 8; 3 4 2 5 7 8 9 1; 3 5 6 7 4 2 4 9; 6 2 3 7 2 9 1 3; 2 4 5 6 1 2 8 9]
D=[1 5 6; 3 5 9; 9 2 4]


printf("A) A i=2 j=3: ")
disp(A(2,3))

printf("B) 2ª linha de B ")
disp(A(2,:))

printf("c) linhas 3 e 5 de C ")
disp(C([3,5],:))

printf("d) o maior elemento de D ")
disp(max(D))

printf("e) A 7ª linha da matriz A com os elementos acrescidos de 2 unidades")
disp((A(7,:))+2)

printf("g) produto do maior elemento de B pelo menor elemento de A")
disp(max(A)*min(B))
