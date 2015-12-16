import csv
import collections

tsv_filename="input.tsv"
csv_filename="output.csv"

# When reading from header row, store in order
tsv_input = []

# uses orderedDict to guarantee column order in output after modifying the 
# associated indeces.
csv_output = collections.OrderedDict()
csv_output["interesting_1"] = -1
csv_output["interesting_2"] = -1

# Identify the columns that require processing
# 'SOURCE_COLUMN' : {'index': INDEX, 'count': #OPTIONS, 'name': 'DEST_COLUMN'}
process_columns = {
    'thing_types' : {'index': -1, 'count':  9, 'name': "Thing Types"},
    'result'         : {'index': -1, 'count':  1, 'name': "Total"}
}


# Allow strings combined for generating new header table
def combine(first, second):
    try:
        return first * second
    except TypeError:
        return '{}*{}'.format(first, second)

# Combines permutations of list items without duplication
# eg ([a, b], [a, b])
# [a, a^2, ab, b, b^2] (note ab != 2ab)
# meant to be used where "second" is a previous permutation of first
def permute(first, second):
    shorter = []
    longer = []
    if len(first) <= len(second):
        shorter = first
        longer = second
    else:
        shorter = second
        longer = first
    output = []
    for i in range(0, len(shorter)):
        for o in range (i, len(longer)):
            output.append(combine(shorter[i], longer[o]))
    return output

# permute a data set to some exponent without duplicate index combinations
# eg polymap([a,b,c], 2) returns:
# [a, b, c, a^2, ab, ac, b^2, bc, c^2]]
def polymap(data_in, exponent):
    data_out = list(data_in)
    last = list(data_in)
    for i in range(1, exponent):
        last = permute(data_in, last)
        data_out.extend(last)
    return data_out

# Converts a CSV listing of id's to a binary array
# eg "1, 4, 5" (with a max index of 5) gives:
# [1, 0, 0, 1, 1]
def breakout_csv_ids(raw_row, process_column):
    # Default to all zeroes
    new_array = [0] * process_column['count']
    items = raw_row[process_column['index']].strip().split(',')
    for item in items:
        try:
            # If we find a usable number, flag that index
            num = int(item)
            new_array[num-1] = 1
        except Exception:
            # Ignore
            pass
    return new_array

def convert_row(raw_row):

    result_row = []

    # First, do we want this row?
    if raw_row[process_columns['deal_breaker']['index']] != "1":
        return []

    # Then, store all specified columns
    for col, index in csv_output.items():
        result_row.append(raw_row[index])
    
    # Append binary breakout
    #result_row.extend(breakout_csv_ids(raw_row, process_columns['thing_types']))
    
    # Append desired result:
    result_row.append(raw_row[process_columns['result']['index']])
    
    return result_row 



with open(tsv_filename,'rb') as tsvin, open(csv_filename, 'wb') as csvout:
    
    tsvin = csv.reader(tsvin, delimiter='\t')
    csvout = csv.writer(csvout, delimiter=',')

    # Reset
    tsc_input = []

    # Skip first line
    next(tsvin)
    
    # Read column names from header line
    headers = next(tsvin)
    for col in headers:
        tsv_input.append(col.strip())

    # Guarantee all specified column names exist in the header
    # And grab their indexes.
    # index call raises exception if not found
    for col, obj in process_columns.items():
        obj['index'] = tsv_input.index(obj['name'])
    for col in csv_output:
        csv_output[col] = tsv_input.index(col)

    # If headers are as expected, process remaining data
    for row in tsvin:
        if (len(row) != len(tsv_input)):
            raise Exception("Row has wrong number of columns: '{}'".format(row))
        new_row = convert_row(row)
        if new_row:
            csvout.writerow(new_row)
