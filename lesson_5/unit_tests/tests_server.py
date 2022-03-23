import argparse
import json
import sys, os
import time
import unittest

sys.path.append(os.path.join(os.getcwd(), '..'))

from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, inet_aton
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, \
    RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT, MAX_CONNECTIONS


class TestGettingConfigs(unittest.TestCase):
    default_addr_server = ''
    port = '7777'
    result_server = ('', 7777)
    response200 = {RESPONSE: 200}
    response400 = {RESPONSE: 400, ERROR: 'Bad Request'}
    message = {ACTION: 200}
    tMsg = 'Привет'

    def SetUp(self):
        pass

    def tearDown(self):
        pass

# ___________Общая часть для client.py и server.py______________________#
    def testGetAddrPortServ(self):
        '''Тестирование корректности считывания параметров IP адреса и номера порта из командной строки для сервера'''
        self.assertEqual(get_addr_port('-a', self.default_addr_server, '-p', self.port), self.result_server)

    def testGetAddrPortClnt(self):
        '''Тестирование корректности считывания параметров IP адреса и номера порта из командной строки для клиента'''
        self.assertEqual(get_addr_port('--addr', self.default_addr_client, '--port', self.port), self.result_client)

    def testEmulateConn(self):
        '''Тестирование соединения между клиентом и сервером.
         В качестве критерия успешности - корректный ответ от сервера'''
        self.assertEqual(emulate_conn(self.tMsg), self.tMsg)
