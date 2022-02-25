# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
# «сетевое программирование», «сокет», «декоратор». Проверить кодировку
# файла по умолчанию. Принудительно открыть файл в формате Unicode и
# вывести его содержимое.


name = "test_file.txt"
words = ["сетевое программирование", "сокет", "декоратор"]

def write_into_file(name, words):
    with open(name, "w") as file:
        file.write('\n'.join(words))

def read_from_file(name):
    from locale import getpreferredencoding
    with open(name, "r", encoding=getpreferredencoding()) as file:
        pr_lines = [print(line) for line in file]


write_into_file(name, words)
read_from_file(name)