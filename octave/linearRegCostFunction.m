function [J, grad] = linearRegCostFunction(theta, X, y, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
%regression with multiple variables
%   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the 
%   cost of using theta as the parameter for linear regression to fit the 
%   data points in X and y. Returns the cost in J and the gradient in grad

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

secondtheta = theta;
secondtheta(1) = 0;
size(X)
size(theta)
J = ((1 / (2 * m)) * sum((X * theta - y).^2)) + ((lambda / (2 * m)) * sum(secondtheta .^ 2));

tempgrad = zeros(size(theta));
for iter = 1:length(theta)
	tempgrad(iter) = (1 / m) * sum(((X * theta) - y) .* X(:, iter)) + ((lambda / m .* secondtheta(iter)));
end
grad = tempgrad;

grad = grad(:);

end
