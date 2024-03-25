//Lista 1
//Exercício 4

for i=1:5
    for j=1:5
       if i > j then
           a(i,j) = i + j
       elseif i < j then
           a(i,j) = (-2)*j
       else
           a(i,j) = 0 
        end   
    end
end

printf("A= ")
disp(a)
