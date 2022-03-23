import argparse
import os
import socket
import sys
import json
import unittest
from pprint import pprint

sys.path.append(os.path.join(os.getcwd(), '..'))

from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT, RESPONDEFAULT_IP_ADDRESSSE

from func_for_test import *



class TestGettingConfigs(unittest.TestCase):
    default_addr_server = ''
    default_addr_client = '127.0.0.1'
    port = '7777'
    result_server = ('', 7777)
    result_client = ('127.0.0.1', 7777)
    IP_wrong = '9999.9999.0.1'
    IP_valid = '127.0.0.1'
    msg_correct = {"IP":"127.0.0.1","port":"8888"}
    msg_wrong = ['IP', "127.0.0.1", "port", "8888"]
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

    def testIPValid(self):
        '''Тестирование функции valid_ip при правильном формате IP адреса'''
        self.assertTrue(valid_ip(self.IP_valid))

    def testIPWrong(self):
        '''Тестирование функции valid_ip при неправильном формате IP адреса'''
        self.assertFalse(valid_ip(self.IP_wrong))

    def testEmulateConn(self):
        '''Тестирование соединения между клиентом и сервером.
         В качестве критерия успешности - корректный ответ от сервера'''
        self.assertEqual(emulate_conn(self.tMsg), self.tMsg)

#______________________Тестирование функций utils.py______________________________#
    def testGetSendMsgCorrectValue(self):
        '''Тестирование корректности обработки функцией get_message
                сообщений от сервера или клиента'''
        self.assertEqual(get_message(send_message(self.msg_correct)), self.msg_correct)

    def testGetSendMsgWrongValue(self):
        '''Тестирование "отсеивания" ответа (response) в неправильном формате (не в dict) '''
        self.assertFalse(get_message(send_message(self.msg_wrong)))

    def testRaiseSendMessage(self):
        '''тестирование возникновения исключения TypeError
        возникающего в функции send_message при попытке отправить сообщение в неправильном формате'''
        self.assertRaises(TypeError, send_message, self.tMsg)



#___________________Тестирование функций client.py______________________________________#
    def testProcessAns200(self):
        self.assertEqual(process_ans(self.response200), '200 : OK')

    def testProcessAns400(self):
        self.assertEqual(process_ans(self.response400), '400 : Bad Request')

    def testProcessAnsExc(self):
        '''Тестирование возникновения исключения ValueError в функции process_ans
        возникающее при некорректном формате сообщения'''
        self.assertRaises(ValueError,process_ans, self.message)

    def testPresense(self):
        presense = create_presence()
        presense[TIME] = 2
        self.assertEqual(presense, {ACTION: PRESENCE, TIME: 2, USER: {ACCOUNT_NAME: 'Guest'}})








if __name__ == '__main__':
    unittest.main()
