//at1
//Exercício 4
a = [2 -25 12 6; 5 -5 8 -5; 12 6 5 9; 5 -10 40 11; 7 9 7 -4]
b = [2 -1 6 -6 1; -10 12 8 14 5; 9 -7 6 5 8; 1 -3 -9 4 -2]
c = [2 5 0 1 4; 3 -9 7 3 6; 10 5 -1 4 -8; -3 2 1 4 2]

m = a*b
n = b+c

printf("m")
disp(m)

printf("n")
disp(n)

printf("m43 + n34 =")
disp(m(4,3)+n(3,4))

printf("m35 - 3*n23 =")
disp(m(3,5)-(3*n(2,3)))