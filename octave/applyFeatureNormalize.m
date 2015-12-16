function [X_norm] = applyFeatureNormalize(X, mu, sigma)
X_norm = X;
for iter = 1:size(X_norm, 1)
	X_norm(iter,:) = X_norm(iter,:) - mu;
	X_norm(iter,:) = X_norm(iter,:) ./ sigma;
end

