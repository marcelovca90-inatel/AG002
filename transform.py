import re

# mappings
rep = \
{
    # age
    '10-19' : '1',
    '20-29' : '2',
    '30-39' : '3',
    '40-49' : '4',
    '50-59' : '5',
    '60-69' : '6',
    '70-79' : '7',
    '80-89' : '8',
    '90-99' : '9',
    # menopause
    'lt40' : '1',
    'ge40' : '2',
    'premeno' : '3',
    # tumor-size
    '0-4' : '1',
    '5-9' : '2',
    '10-14' : '3',
    '15-19' : '4',
    '20-24' : '5',
    '25-29' : '6',
    '30-34' : '7',
    '35-39' : '8',
    '40-44' : '9',
    '45-49' : '10',
    '50-54' : '11',
    '55-59' : '12',
    # inv-nodes
    '0-2' : '1',
    '3-5' : '2',
    '6-8' : '3',
    '9-11' : '4',
    '12-14' : '5',
    '15-17' : '6',
    '18-20' : '7',
    '21-23' : '8',
    '24-26' : '9',
    '27-29' : '10',
    '30-32' : '11',
    '33-35' : '12',
    '36-39' : '13',
    # node-caps
    'no' : '1',
    'yes' : '2',
    # deg-malig
    '1' : '1',
    '2' : '2',
    '3' : '3',
    # breast
    'left' : '1',
    'right' : '2',
    # breast-quad
    'left_up' : '1',
    'left_low' : '2',
    'right_up' : '3',
    'right_low' : '4',
    'central' : '5',
    # class
    'no-recurrence-events' : '1',
    'recurrence-events' : '2'
}

file_in = open('breast-cancer-orig.csv', 'r')
file_out = open('breast-cancer-proc.csv', 'w')
count = 0
 
missing = 0
for line in file_in:
    count += 1
    if 'age' in line:
        print('Header detected; copying to output.\n\n')
        file_out.write(line)
    elif '?' in line:
        missing += 1
        print(f'Line {count} contains a missing value and will be ignored.\n\n')
    else:
        parts = line.strip().split(',')
        transf = [rep[p] for p in parts]
        print(f'Line {count}\nSource = {parts}\nTransf = {transf}\n\n')
        replaced = re.sub('[\\[\\]\\ ]','',str([int(p) for p in transf]))
        file_out.write(f'{replaced}\n')
        
file_in.close()
file_out.close()

print(f'{missing} lines with missing values were found.')