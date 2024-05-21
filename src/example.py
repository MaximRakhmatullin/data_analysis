lines = ['hello', 'world', 'python', 'code']
numbers = [1, 2, 3, 4, 5]
nums = ['12', '34', '543']

words_str = ';\n'.join(lines)
print(tuple(map(int, nums)))
numbers_str = ', '.join(map(str, numbers))
print(numbers_str)

line = 'word 1: ' + lines[0] + ', word 2: ' + lines[1]
line2 = f'word 1: {lines[0]}, word 2: {lines[1]}'

print('hello world'.title())

print(line)
print(line2)
print(f'sorted words: {sorted(lines)}')
print(f'{sorted(lines) = }')
# print(words_str)
