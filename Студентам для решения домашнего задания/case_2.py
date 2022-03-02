'''2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с
информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными.'''
import json


def write_order_to_json(cart):
    with open('orders.json') as f_n:
        dict = json.load(f_n)
        print(dict)
        dict['orders'].append(cart)
    with open('orders.json', 'w') as f_w:
        json.dump(dict, f_w, indent=4)


write_order_to_json({'item': 'Printer', 'quantity': 1, 'price': 250, 'buyer': 'Ivanovich', 'date': '02.03.2022'})
write_order_to_json({'item': 'Monitor', 'quantity': 1, 'price': 758, 'buyer': 'Ivanovich', 'date': '02.03.2022'})
write_order_to_json({'item': 'Notebook', 'quantity': 1, 'price': 356, 'buyer': 'Ivanovich', 'date': '02.03.2022'})
write_order_to_json({'item': 'Server', 'quantity': 1, 'price': 965, 'buyer': 'Ivanovich', 'date': '02.03.2022'})