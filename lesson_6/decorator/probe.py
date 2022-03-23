# import inspect
# import traceback
#
# #
# # def say_my_name():
# #     stack = traceback.extract_stack()
# #     print('Print from {}'.format(stack[-2][2]))
# #
# # def say_his_name():
# #     from inspect import stack
# #     return inspect.stack()[3][1]
# #
# # def probe():
# #     say_my_name()
# #
# # def wrap(func):
# #     print(func.__name__)
# #     return say_his_name()
# #
# # print(wrap(say_his_name))
# # probe()
#
# import functools
# from datetime import datetime
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         # Преобразуем в строку имена аргументов и их значения
#         func_name = func.__name__
#         master_name_func = inspect.stack()[1][3]
#         print("Time: ", datetime.now().strftime("%Y-%m-%d [%H:%M:%S]"))
#         print("func_name: ", func_name )
#         print("master_name_func: ", master_name_func)
#         return func(*args, **kwargs)
#
#     return wrapper
# @log
# def divint(a, b):
#     return a / b
#
# def master(a,b):
#     return divint(a, b)
#
# divint(4, 2)

import functools
import sys

sys.path.append('../')
from logs.config_client_log import LOGGER

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_rep = [repr(arg) for arg in args]
        kwargs_rep = [f"{k}={v!r}" for k, v in kwargs.items()]
        sig = ", ".join(args_rep + kwargs_rep)
        val = func(*args, **kwargs)
        val = val.upper() + "!"
        return val
    return wrapper
@log
def hello(name):
    "Hello from the other side."
    return f"Hello {name}"