clear all;
close all;

load("DCbasico.mat")    %carga de datos

media = 5;
sigma = 1;


%% a

X1 = X(1:10); x= 0 % prueba
X2 = X(11:20); x= 0; prueba=9;
X3 = X(21:30);
X4 = X(31:40);


X1_m = mean(X1)
X2_m = mean(X2)
X3_m = mean(X3)
X4_m = mean(X4)

%% b

X1_var = var(X1)
X2_var = var(X2)
X3_var = var(X3)
X4_var = var(X4)


%% c

N = [100 200 1000 2500; 5000 7000 8000 10000]

for i = 1:length(N)
    
    X_vector = X(1:N(i))
    
    X_mean(i) = mean(X_vector)
    X_var(i) = var(X_vector)

end

figure(1)
plot(N, X_mean)
title("media")
xlabel("muestras")
ylabel("media")
figure(2)
plot(N, X_var)
title("varianza")
xlabel("muestras")
ylabel("varianza")