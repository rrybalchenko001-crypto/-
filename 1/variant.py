# 1. Запрос названия заказа и имени заказчика
order_name = input("Название заказа: ")
client_name = input("Имя заказчика: ")

# 2. Ввод позиций
item1_name = input("Название 1-го товара: ")
item1_count = int(input("Количество 1-го товара: "))
item1_price = float(input("Цена 1-го товара: "))

item2_name = input("Название 2-го товара: ")
item2_count = int(input("Количество 2-го товара: "))
item2_price = float(input("Цена 2-го товара: "))

# 3. Ввод скидки, доставки и внесенной суммы
discount_percent = float(input("Скидка в % (от 0 до 100): "))
delivery_cost = float(input("Стоимость доставки: "))
paid_amount = float(input("Внесённая сумма: "))

# 4. Расчеты
item1_total = item1_count * item1_price
item2_total = item2_count * item2_price

goods_total = item1_total + item2_total
discount_rubles = goods_total * (discount_percent / 100)
goods_with_discount = goods_total - discount_rubles

grand_total = goods_with_discount + delivery_cost
total_count = item1_count + item2_count
change = paid_amount - grand_total

# 5. Вывод
print(f"\n=== ЗАКАЗ: {order_name} ===")
print(f"Заказчик: {client_name}")
print(f"{item1_name} | {item1_count} шт. | {item1_price:.2f} руб. | {item1_total:.2f} руб.")
print(f"{item2_name} | {item2_count} шт. | {item2_price:.2f} руб. | {item2_total:.2f} руб.")
print("-" * 30)
print(f"Общее количество товаров: {total_count} шт.")
print(f"Стоимость товаров без скидки: {goods_total:.2f} руб.")
print(f"Скидка ({discount_percent:.0f}%): {discount_rubles:.2f} руб.")
print(f"Стоимость товаров со скидкой: {goods_with_discount:.2f} руб.")
print(f"Доставка: {delivery_cost:.2f} руб.")
print(f"Итого к оплате: {grand_total:.2f} руб.")
print(f"Внесено: {paid_amount:.2f} руб.")
print(f"Сдача: {change:.2f} руб.")