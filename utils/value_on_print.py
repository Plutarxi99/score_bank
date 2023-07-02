import datetime
import re

def value_on_print(list_for_value):
    """
    Цикл для выводы списка операции по очереди
    :param list_for_value: получает на вход список операции, который надо выввести
    :return:
    """
    for x in range(len(list_for_value)):
        data = formatted_time(list_for_value[x]["date"])
        card_number = (list_for_value[x].get('from', ''))
        print(f'''
        {data} {list_for_value[x]["description"]}
        {formatted_card_number(card_number)}->{list_for_value[x]["to"]}
        {list_for_value[x]['operationAmount']["amount"]} {list_for_value[x]['operationAmount']['currency']["name"]}
        ''')
        input()
        continue

def formatted_time(data):
    """
    Форматирует нужный формат даты
    :param data:
    :return:
    """
    date = datetime.datetime.fromisoformat(data)
    date_f = date.strftime("%d.%m.%Y")
    return date_f

def formatted_card_number(card_number):
    number = []
    name_card = []
    for x in card_number:
        if x.isdigit():
            number.append(x)
        else:
            name_card.append(x)
    s = "".join(number)
    res = " ".join(s[i * 4: i * 4 + 4] for i in range(len(s) // 4))

    a = "*"
    b = a * int(len(res))
    cod = res[0:7] + b + res[-4:]
    return f'{"".join(name_card)} {cod}'

