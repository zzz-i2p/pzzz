# -*- coding: utf-8 -*-
"""
* Пример вопрос чекбокс 
* пример выполнения, вводя `python example/checkbox.py` в консоли
"""
from __future__ import print_function, unicode_literals

from pprint import pprint

from PyInquirer import style_from_dict, Token, prompt, Separator

from examples import custom_style_2


questions = [
    {
        'type': 'checkbox',
        'qmark': '😃',
        'message': 'Select toppings',
        'name': 'toppings',
        'choices': [ 
            Separator('= Мясо ='),
            {
                'name': 'Ham'
            },
            {
                'name': 'Ground Meat'
            },
            {
                'name': 'Bacon'
            },
            Separator('= Сыры ='),
            {
                'name': 'Моцарелла',
                'checked': True
            },
            {
                'name': 'Чеддер'
            },
            {
                'name': 'Пармезан'
            },
            Separator('= Обычная ='),
            {
                'name': 'Гриб'
            },
            {
                'name': 'Tomato'
            },
            {
                'name': 'Pepperoni'
            },
            Separator('= The extras ='),
            {
                'name': 'Pineapple'
            },
            {
                'name': 'Olives',
                'disabled': 'out of stock'
            },
            {
                'name': 'Extra cheese'
            }
        ],
        'validate': lambda answer: 'Вы должны выбрать по крайней мере один топпинг.' \
            if len(answer) == 0 else True
    }
]

answers = prompt(questions, style=custom_style_2)
pprint(answers)