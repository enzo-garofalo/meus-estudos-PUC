P = [1/2 1/3 1/2; 0 1/3 2/3; 1/2 1/3 0]
X0 = [120 180 90]'
X = zeros(3,3)

for j=1:3
    X(:,j) = P^j*X0 
end

printf("x1 =")
disp(X(:,1))

printf("x2 =")
disp(X(:,2))

printf("x3 =")
disp(X(:,3))
