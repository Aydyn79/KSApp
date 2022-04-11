"""
Следующий пример: контроль имён атрибутов вновь созданного класса Foo
с помощью метакласса ControlAttrName
"""
import sys
from pprint import pprint
sys.path.append('../logs/')

class ControlAttrName(type):
    # Вызывается для создания экземпляра класса, перед вызовом __init__
    def __init__(cls, future_class_name, future_class_parents, future_class_attrs):
        """
          Метод проверяет наличие атрибутов из списка required_attributes.
          По умолчанию - ни один из обязательных атрибутов не найден
          (изначально список not_found_attributes == required_attributes).
        """
        required_attributes = ['account_name', 'sock']
        not_found_attributes = required_attributes.copy()
        for attr, v in future_class_attrs.items():
            if attr in required_attributes:
                not_found_attributes.remove(attr)

        if not_found_attributes:
            raise AttributeError(f"Not found attributes: {', '.join(not_found_attributes)}")

        super(ControlAttrName, cls).__init__(future_class_name,
                                             future_class_parents,
                                             future_class_attrs)

#
# class Foo(metaclass=ControlAttrName):
#     x = 5
#
#
# foo = Foo()


