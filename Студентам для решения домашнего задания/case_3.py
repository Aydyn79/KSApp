'''Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий
сохранение данных в файле YAML-формата.'''
import yaml
data = {'1-й': [10,20,30,40], '2-й': 1, '3-й': {'f':[10,20,30,40], 's': 1}}


with open('file.yaml', 'w') as f_n:
    yaml.dump(data, f_n, default_flow_style=False, allow_unicode = True)

with open('file.yaml') as f_n:
    f_n_content = yaml.safe_load(f_n)

print(f_n_content == data)


  

  