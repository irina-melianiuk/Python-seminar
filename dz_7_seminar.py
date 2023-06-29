input_str = input()
vowel_letter = {'а', 'о', 'е', 'у', 'ё', 'ы', 'и', 'э', 'ю', 'я'}
some_list = input_str.split()

result_set = set()

for word in some_list:
count = 0
for letter in word:
if letter in vowel_letter:
count += 1
result_set.add(count)

if len(result_set) == 1:
print('Парам пам-пам')
else:
print('Пам парам')

###
def print_operation_table(operation, num_rows=6, num_columns=6):
for row in range(1, num_rows + 1):
for col in range(1, num_columns + 1):
print(round(operation(row, col), 1), end='\t')
print()


print_operation_table(lambda x, y: x * y)