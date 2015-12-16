import math
import csv

csv_filename="output.csv"
csf = 0.5


def compute_cost(x, y, m):
    return math.pow( (x-y), 2) / (2*m)

with open(csv_filename,'rb') as csvfile:
    csvin = csv.reader(csvfile, delimiter=',')
    
    cost = 0
    avg_factor = 0
    row_count = sum(1 for row in csvin)
    # 'reset' csv file to re-iterate
    csvfile.seek(0)
    for row in csvin:
        scalar = 1
        col_count = len(row)
        y = float(row[col_count-1])
        for index, value in enumerate(row):
            if (index < col_count-1):
                scalar *= float(value)
        #print("Scalar: {}, y: {}, y/scalar: {}".format(scalar, y, y/scalar))
        cost += compute_cost(scalar * csf, y, row_count)
        avg_factor += (y/scalar) / row_count

    print("Cost with CSF({}): {}".format(csf, cost))
    print("avg calc csf: {}".format(avg_factor))

