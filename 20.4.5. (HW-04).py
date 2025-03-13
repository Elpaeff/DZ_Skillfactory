import json

with open("orders_july_2023.json", "r") as my_file:
    orders = json.load(my_file)
    max_price = 0
    max_order = ''
    # цикл по заказам
    for order_num, orders_data in orders.items():
        # получаем стоимость заказа
        price = orders_data['price']
        # если стоимость больше максимальной - запоминаем номер и стоимость заказа
        if price > max_price:
            max_order = order_num
            max_price = price
    print(f'Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')