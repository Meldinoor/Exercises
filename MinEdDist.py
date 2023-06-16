import numpy as np

WORD_1 = input('Please insert the first word.\n')
WORD_2 = input('Please input the second word.\n')

def insert_cost(char):
    return 1

def delete_cost(char):
    return 1

def substitution_cost(char1, char2):
    return 0 if char1 == char2 else 2

def print_cell(cell):
    print(chr(0x2190) if 'ins' in cell['steps'] else ' ', end='')
    print(chr(0x2191) if 'del' in cell['steps'] else ' ', end='')
    print(chr(0x2196) if 'sub' in cell['steps'] else ' ', end='')
    print(f'{cell["distance"]}|', end='')

med_matrix = [[{ 'distance': 0, 'steps': [] }]]

for i in range(1, len(WORD_1) + 1):
    med_matrix.append([{ 'distance': i, 'steps': ['del'] }])

for i in range(1, len(WORD_2) + 1):
    med_matrix[0].append({ 'distance': i, 'steps': ['ins'] })

for i in range(1, len(WORD_1) + 1):
    for j in range(1, len(WORD_2) + 1):
        ins_cost = med_matrix[i][j-1]['distance'] + insert_cost(WORD_2[j-1])
        del_cost = med_matrix[i-1][j]['distance'] + delete_cost(WORD_1[i-1])
        sub_cost = med_matrix[i-1][j-1]['distance'] + substitution_cost(WORD_1[i-1], WORD_2[j-1])

        min_cost = np.min([ins_cost, del_cost, sub_cost])
        cell = { 'distance': min_cost, 'steps': [] }

        if ins_cost == min_cost:
            cell['steps'].append('ins')
        if del_cost == min_cost:
            cell['steps'].append('del')
        if sub_cost == min_cost:
            cell['steps'].append('sub')

        med_matrix[i].append(cell)

# for i in range(len(med_matrix)):
#     if i == 0:
#         print('      *', end='')
#         print(''.join(list(f'    {x}' for x in WORD_2)))
#     print(' * ' if i == 0 else f' {WORD_1[i-1]} ', end='')
#     for j in range(len(med_matrix[i])):
#         print_cell(med_matrix[i][j])
#     print('')

#Backtrace
cell = med_matrix[len(WORD_1)][len(WORD_2)]
ops = []
i = len(WORD_1)
j = len(WORD_2)

while len(cell['steps']) > 0:
    if 'sub' in cell['steps']:
        ops.insert(0, { 'op': 'sub', 'from': WORD_1[i-1], 'to': WORD_2[j-1] })
        i = i-1
        j = j-1
        cell = med_matrix[i][j]
    elif 'ins' in cell['steps']: 
        ops.insert(0, { 'op': 'ins', 'char': WORD_2[j-1] })
        j = j-1
        cell = med_matrix[i][j]
    else:
        ops.insert(0, { 'op': 'del', 'char': WORD_1[i-1] })
        i = i-1
        cell = med_matrix[i][j]

print('Output:')
print('----------------')
print('')

i = 0
for op in ops:
    if op['op'] == 'sub' or op['op'] == 'del':
        print(WORD_1[i], end='')
        i = i + 1
    else: 
        print('*', end='')

print('')
print(''.join(list(chr(0x2193) for _ in ops)))

i = 0
for op in ops:
    if op['op'] == 'sub' or op['op'] == 'ins':
        print(WORD_2[i], end='')
        i = i + 1
    else: 
        print('*', end='')

print(''.join(list()))

print('')
print(f'The minimum edit distance is: {med_matrix[len(WORD_1)][len(WORD_2)]["distance"]}')
print('\n\n\n')