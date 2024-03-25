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

soma = 0
for j=1:6 
        soma = soma + A(1,j)
end
printf("A) SOMA DOS ELEMENTOS DA PRIMEIRA LINHA.")
disp(soma)

maximo = A(1,4)
for i=1:10
    if A(i,4) > maximo then
        maximo = A(i,4)
        indice = i
    end
end
printf("B) DETERMINE O ELEMENTO MÁXIMO DA QUARTA COLUNA E SEUS RESPECTIVOS ÍNDICES.")
disp(maximo)
printf("Indices J = 4 e I = ")
disp(indice)

minimo = A(2,1)
for j=1:6
    if A(2,j) < minimo then
        minimo = A(2,j)
        indice = j
    end
end
printf("C) DETERMINE O ELEMENTO MÍNIMO DA SEGUNDA LINHA E SEUS RESPECTIVOS ÍNDICES.")
disp(minimo)
printf("Indices i = 2 e j = ")
disp(indice)
