'''5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
байтовового в строковый тип на кириллице.'''

import chardet, subprocess, platform

param = '-n' if platform.system().lower() == 'windows' else '-c'
args1 = ['ping', param, '2', 'yandex.ru']
args2 = ['ping', param, '2', 'youtube.com']

def ping_decode(args):
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in process.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))

ping_decode(args1)
ping_decode(args2)
