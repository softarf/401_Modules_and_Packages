# -*- coding: utf-8 -*-
#                       "Подготовка к собеседованию".
#                   Задача №2. Импорт функций в модуль main.py и вызов их.

from typing import List, Any

import data
from application import salary
from application.db.people import Employee


def enterprise_tax(all_employees: List[Any]) -> float:
    """Вычисляет сумму налога."""
    payroll: float = 0
    employee: Any
    for employee in all_employees:
        payroll += employee.income
    print('\nВыполнена процедура enterprise_tax(), модуль main.py')
    return payroll * 13 / 100


def main():
    """Осуществляет подготовку исходных данных и вывод результата выполнения."""
    full_list: List[Any] = Employee.get_employees(data.employees_list)
    salary.calculate_salary(full_list, 21)
    res: float = enterprise_tax(full_list)
    print('\nВыполнена процедура main(), модуль main.py')
    print(f'Результат: {res}')


if __name__ == '__main__':
    main()
    # input('\n  -- Конец --  ')  # Типа  "Пауза" - Для среды
