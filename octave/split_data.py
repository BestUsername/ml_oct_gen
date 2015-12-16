import random

input_filename = 'output.csv'

output_train = "train.csv"
output_test = "test.csv"

# Only a rough estimate
train_percent = .7

with open(input_filename, 'rb') as source, open(output_train, 'wb') as dest1, open(output_test, 'wb') as dest2:
    for line in source:
         if random.random() < train_percent:
             dest1.write(line)
         else:
             dest2.write(line)
