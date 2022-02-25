'''3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
байтовом типе.'''

wr_seq = ['attribute', 'класс', 'функция', 'type']
for s in wr_seq:
    try:
        print(eval('b'+'"' + s + '"'))
    except SyntaxError:
        print('"' + s + '"' + ' невозможно записать в байтовом типе.')
