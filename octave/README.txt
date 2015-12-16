regularized polynomial regression

Take features (f1, f2, ... fn) and desired result y
generate model (t0, t1, t2, ... tn) to be applied like:
t0 + t1*f1 + t2*f2 + ... tn*fn
And train to minimize the difference between that equation and y.

Regularized - prevent over-fiting by adding a cost to theta size in the cost function
Polynomial  - extrapolate new features by combining existing ones

Steps:
.) load data
X) break data into training / testing sets
.) normalize features (store mu/sigma for scaling future data to the model)
.) Fix NaN entries from normalizing all-zero columns
X) permute new features from existing
.) Add 1's column because math
.) calculate initial costs on training set (regularized and normal)
.) train model
.) calculate trained costs on training set (regularized and normal)
X) calculate trained costs on testing set
.) calculate 


Run:

octave regpolyreg.m
