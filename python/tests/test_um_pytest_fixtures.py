from unnecessary_math import multiply


def setup_module(module):
    print("setup_module      module:%s" % module.__name__)


def teardown_module(module):
    print("teardown_module   module:%s" % module.__name__)


def setup_function(function):
    print("setup_function    function:%s" % function.__name__)


def teardown_function(function):
    print("teardown_function function:%s" % function.__name__)


def test_numbers_3_4():
    print('test_numbers_3_4  <============================ actual test code')
    assert multiply(3, 4) == 12


def test_strings_a_3():
    print('test_strings_a_3  <============================ actual test code')
    assert multiply('a', 3) == 'aaa'


class TestUM:
    @staticmethod
    def setup():
        print("setup             class:TestStuff")

    @staticmethod
    def teardown():
        print("teardown          class:TestStuff")

    def setup_class(self):
        print("setup_class       class:%s" % self.__name__)

    def teardown_class(self):
        print("teardown_class    class:%s" % self.__name__)

    @staticmethod
    def setup_method(method):
        print("setup_method      method:%s" % method.__name__)

    @staticmethod
    def teardown_method(method):
        print("teardown_method   method:%s" % method.__name__)

    @staticmethod
    def test_numbers_5_6():
        print(
            'test_numbers_5_6  <============================ actual test code')
        assert multiply(5, 6) == 30

    @staticmethod
    def test_strings_b_2():
        print(
            'test_strings_b_2  <============================ actual test code')
        assert multiply('b', 2) == 'bb'
