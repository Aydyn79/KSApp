import argparse
import json
import sys, os
import time

sys.path.append(os.path.join(os.getcwd(), '..'))

from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, inet_aton
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, \
    RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT, MAX_CONNECTIONS


def get_addr_port(n_addr, value_addr, n_port, value_port):
    '''Выпилил кусок кода парсящий параметры коммандной строки и возвращающий
    значения порта и IP адреса и сделал из него функцию для тестирования'''
    parser = argparse.ArgumentParser()
    parser.add_argument(n_addr, nargs='?', default="")
    parser.add_argument(n_port, nargs='?', default='7777')
    args = parser.parse_args([n_addr, value_addr, n_port, value_port])
    param_names = [param_name for param_name, _ in vars(args).items()]
    try:
        if 'port' in param_names:
            listen_port = int(args.port)
        elif 'p' in param_names:
            listen_port = int(args.p)
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except TypeError:
        print('После параметра -\'p\' необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        print(
            'В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)
    try:
        if 'addr' in param_names:
            listen_address = args.addr
        elif 'a' in param_names:
            listen_address = args.a
    except IndexError:
        print(
            'После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)
    return listen_address, listen_port


def process_ans(message):
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError

def create_presence(account_name='Guest'):
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out

def valid_ip(address):
    try:
        if inet_aton(address):
            return True
    except OSError:
        if address == 'localhost':
            return True
        else:
            return False


def get_message(client_response):
    if isinstance(client_response, bytes):
        json_response = client_response.decode('utf-8')
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


def send_message(message):
    if not isinstance(message, dict):
        raise TypeError
    js_message = json.dumps(message)
    return js_message.encode('utf-8')

def emulate_conn(message):# Создаем тестовый сокет для сервера
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind((DEFAULT_IP_ADDRESS, DEFAULT_PORT))
    server_socket.listen(MAX_CONNECTIONS)

    # Создаем тестовый сокет для клиента
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((DEFAULT_IP_ADDRESS, DEFAULT_PORT))

    # Отправляем и получаем сообщение
    client, address = server_socket.accept()
    msg = message.encode('utf-8')
    client_socket.send(msg)
    answer = client.recv(1024)
    client.close()
    client_socket.close()
    server_socket.close()
    return answer.decode('utf-8')
