//at1
//Exercício 8

for i=1:3
    for j=1:4
        if i > j then
            a(i,j) = 2*i
        elseif i < j then
            a(i,j) = i + j
        else
            a(i,j) = i - 1
        end
    end
end

printf("a = ")
disp(a)

printf("soma dos elementos da 1ª linha: ")
disp(sum(a(1,:)))

printf("soma dos elementos da 4ª coluna: ")
disp(sum(a(:,4)))
