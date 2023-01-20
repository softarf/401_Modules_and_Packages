# -*- coding: utf-8 -*-
#                       ДЗ 1. "Модули, пакеты, импорты в Python".
#               Задача №1. Класс "Сотрудник".
#
from typing import List, Any


class Employee:
    """
    Абстрактный тип, представляющий собой поля данных сотрудника.
    """

    def __init__(self, all_fields: List[Any]) -> None:
        """Создаёт карточку заданного сотрудника."""
        self.name: str = all_fields[0]
        self.position: str = all_fields[1]
        self.salary: int = all_fields[2]
        self.income: float = 0

    def get_employees(all_employees: List[Any]) -> List[Any]:
        """Возвращает список всех сотрудников."""
        full_list: List[Any] = []
        employee: Any
        for employee in all_employees:
            full_list.append(Employee(employee))
        print('\nВыполнен метод класса Employee.get_employees(), модуль people.py')
        return full_list
