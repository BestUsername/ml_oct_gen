%% ================ Part 1: Feature Normalization ================

%% Clear and Close Figures
clear ; close all; clc

file_train = 'train.csv';
file_test = 'test.csv';

%% Load Training Data
fprintf('Loading Training data from %s\n', file_train);
data = load(file_train);
%% Get data dimensions and break into features matrix and result vector
[m, n] = size(data);
X = data(:, 1:(n-1));
y = data(:, n);

% Scale features and set them to zero mean
fprintf('Normalizing Features\n');
[X mu sigma] = featureNormalize(X);

% remove NaN for /0 errors
X(isnan(X))=0;

% Add intercept term to X
X = [ones(m, 1) X];

%% ================ Part 2: Compute initial costfunctions ================

% Set number of iterations for gradient descent
num_iters = 400;
% Set regularization parameter lambda to 1
lambda = 1;

% Initialize fitting parameters
theta = zeros(n, 1);

% Compute and display initial costs
cost = computeCostMulti(X, y, theta);

fprintf('Cost of initial theta (zeros): %f\n', cost);

%% ================ Part 3: Train ================

% Set Options
options = optimset('GradObj', 'on', 'MaxIter', num_iters);

fprintf('Training model\n');
% Optimize
[theta, J, exit_flag] = ...
	fminunc(@(t)(linearRegCostFunction(t, X, y, lambda)), theta, options);

% Compute and display trained costs
cost = computeCostMulti(X, y, theta);

fprintf('Cost of trained theta: %f\n', cost);

%% ================ Part 4: Review ================

%% Load Testing Data
fprintf('Loading Testing data from %s\n', file_test);
data = load(file_test);
%% Get data dimensions and break into features matrix and result vector
[m, n] = size(data);
X = data(:, 1:(n-1));
y = data(:, n);

% Scale features and set them to zero mean
fprintf('Normalizing Features\n');
% use previous feature normalization parameters
X = applyFeatureNormalize(X, mu, sigma);

% remove NaN for /0 errors
X(isnan(X))=0;

% Add intercept term to X
X = [ones(m, 1) X];

% compute cost using previous model and new testing data
cost = computeCostMulti(X, y, theta);

fprintf('Cost on testing data: %f\n', cost)
