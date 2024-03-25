//Monte a matriz A-10x6 definida por:

for i=1:10
    for j=1:6
        if i > j then
            A(i,j) = 2*i
        elseif i < j then
            A(i,j) = i+j
        else
            A(i,j) = i - 1
        end
    end
end

printf("A = ")
disp(A)

printf("A) SOMA DOS ELEMENTOS DA PRIMEIRA LINHA.")
disp(sum(A(1,:)))


printf("B) DETERMINE O ELEMENTO MÁXIMO DA QUARTA COLUNA E SEUS RESPECTIVOS ÍNDICES.")
disp(max(A(:,4)))

printf("C) DETERMINE O ELEMENTO MÍNIMO DA SEGUNDA LINHA E SEUS RESPECTIVOS ÍNDICES.")
disp(min(A(2,:)))

printf("Indices i = 2 e j = ")
disp(indice)
