'''2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
последовательность кодов (не используя методы encode и decode) и определить тип,
содержимое и длину соответствующих переменных.'''
seq = ['class', 'function', 'method']

b_seq = [eval('b'+'"' + s + '"') for s in seq]
print(*b_seq, sep=', ')
print(*list(map(len, b_seq)), sep=', ')
print(*list(map(type, b_seq)), sep=', ')