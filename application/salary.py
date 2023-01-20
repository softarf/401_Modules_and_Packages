# -*- coding: utf-8 -*-
#                       ДЗ "Модули, пакеты, импорты в Python".
#               Задача №1. Модуль расчёта зарплаты.
#
from typing import List, Any


def calculate_salary(all_employees: Any, working_days: int) -> float:
    """Возвращает сумму налога."""
    payroll: int = 0
    employee: Any
    for employee in all_employees:
        employee.income = employee.salary * working_days / 30
    income_tax: float = payroll * 13 / 100
    print('\nВыполнена процедура calculate_salary(), модуль salary.py')
    return income_tax
