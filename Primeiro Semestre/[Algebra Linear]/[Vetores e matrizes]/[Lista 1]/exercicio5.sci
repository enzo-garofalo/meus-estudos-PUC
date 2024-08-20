//Lista 1
//Exercício 5

for i=1:6
    for j=1:7
        if i > j then
           a(i,j)=(-2)*i +(3*j)
        elseif i < j then
           a(i,j)=(5*i)-j
        else
            a(i,j)=0
        end
    end
end

printf("A= ")
disp(a)
