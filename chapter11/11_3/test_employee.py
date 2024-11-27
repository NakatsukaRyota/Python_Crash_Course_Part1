import pytest
from employee import Employee

@pytest.fixture
def employee_info():
    employee_info = Employee("良太", "中塚", 1000000)
    return employee_info

def test_give_default_raise(employee_info):
    employee_info.give_raise()
    assert employee_info.income == 1500000

def test_give_custom_raise(employee_info):
    employee_info.give_raise(1000000)
    assert employee_info.income == 2000000
