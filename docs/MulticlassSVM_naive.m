clear all
clc

load wine_dataset
x = wineInputs;
y = wineTargets;
delta = 1;
lamda = 0.3;
learning_rate = 0.2;

%% Correct class
correct_class = zeros(1,size(y,2));

for i = 1:size(y,2)
    for j = 1:size(y,1)
        if y(j,i) ~= 0
            correct_class(i) = j;
        end
    end
end

w = (0.5-(-0.5))*rand(13,3)+(-0.5);

% Bias trick
bias1 = ones(1,size(w,2));
W = [w; bias1 ];
bias = ones(1,size(x,2));
X = [x; bias];

%% Train
num_classes = size(y,1);
num_trains = size(X,2);
num_iter = 100;
dW = zeros(size(W,1),size(W,2));
    
loss_history = zeros(1,num_iter);
loss = 0;
count = 0;

for k = 1:num_iter
    scores = W'*X;
for i = 1:num_trains
    correct_class_score = scores(correct_class(i),i);
    num_sup_zero = 0;
    for j = 1:num_classes
        if j ~= correct_class(i)
%             continue
            margin = scores(j,i) - correct_class_score + delta;
            if margin > 0
                num_sup_zero = num_sup_zero + 1;
                loss = loss + margin;
                dW(:,j) = dW(:,j) + X(:,i);
%                 dW(:,correct_class(i)) = dW(:,correct_class(i)) - X(:,i);
            end
        end
    end
     dW(:,correct_class(i)) = dW(:,correct_class(i)) - num_sup_zero*X(:,i);
      
end

loss = loss/num_trains;

regularization = 0;
for i = 1:size(W,1)
    for j = 1:size(W,2)
        regularization = regularization + W(i,j)^2;
    end
end

loss = loss + 0.5*lamda*regularization;

dW = dW/num_trains;
dW = dW + lamda*W;

loss_history(k) = loss;

W = W - learning_rate.*dW;
% w = W(1:(size(W,1)-1),:);
end    


    
    
    