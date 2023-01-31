# -*- coding: utf-8 -*-
#                       "Модули и пакеты. Импорт."
#                   Задача №1. Разработать структуру программы "Бухгалтерия".
#                   Задача №2. Импорт функций в модуль main.py и вызов их.
#                   Задача №3. При вызове функций модуля main.py выводить текущую дату.

from typing import List, Any

import data
from application import salary
from application.db.people import Employee

import math
from datetime import datetime


def enterprise_tax(all_employees: List[Any]) -> int:
    """Вычисляет сумму налога."""
    payroll: float = 0
    employee: Any
    for employee in all_employees:
        payroll += employee.income
    print('\nВыполнена процедура enterprise_tax(), модуль main.py')

    return math.floor(payroll * 13 / 100 + 0.5)


def main():
    """Осуществляет подготовку исходных данных и вывод результата выполнения."""
    full_list: List[Any] = Employee.get_employees(data.employees_list)
    salary.calculate_salary(full_list, 21)
    res: int = enterprise_tax(full_list)
    print('\nВыполнена процедура main(), модуль main.py')
    # Работа с модулем datetime.
    today: datetime = datetime.today()
    day: str = today.strftime('%d')
    month: str = today.strftime('%b')
    year: str = today.strftime('%Y')
    print(f'Сегодня: {day} {month} {year}')

    print(f'Результат: {res}')


if __name__ == '__main__':
    main()
    # input('\n  -- Конец --  ')  # Типа  "Пауза" - Для среды
