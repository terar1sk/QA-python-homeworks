#alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)

print("=== Task 01 ===")
print("Переменная alice_in_wonderland занимает несколько строк кода\n")

print("=== Task 02 ===")
count_quotes = 0
for ch in alice_in_wonderland:
    if ch == "'":
        print(ch)
        count_quotes += 1
print("Всего одинарных кавычек найдено:", count_quotes, "\n")

print("=== Task 03 ===")
print(alice_in_wonderland, "\n")


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""

# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
print("=== Task 04 ===")
black_sea = 436402
azov_sea = 37800
total = black_sea + azov_sea
print("Черное и Азовское моря вместе занимают", total, "км^2.\n")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
print("=== Task 05 ===")
total_all = 375291
a_plus_b = 250449
b_plus_c = 222950

a = total_all - b_plus_c
b = a_plus_b - a
c = b_plus_c - b

print("На первом складе:", a)
print("На втором складе:", b)
print("На третьем складе:", c, "\n")


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
print("=== Task 06 ===")
months = 18
payment_per_month = 1179
price = months * payment_per_month
print("Компьютер стоит", price, "грн\n")


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print("=== Task 07 ===")
print("Остаток от деления 8019 на 8 =", 8019 % 8)
print("Остаток от деления 9907 на 9 =", 9907 % 9)
print("Остаток от деления 2789 на 5 =", 2789 % 5)
print("Остаток от деления 7248 на 6 =", 7248 % 6)
print("Остаток от деления 7128 на 5 =", 7128 % 5)
print("Остаток от деления 19224 на 9 =", 19224 % 9, "\n")


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
print("=== Task 08 ===")
pizza_big = 4 * 274
pizza_mid = 2 * 218
juice = 4 * 35
cake = 350
water = 3 * 21

order_total = pizza_big + pizza_mid + juice + cake + water
print("На заказ ко дню рождения нужно", order_total, "грн\n")



# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
print("=== Task 09 ===")
photos = 232
per_page = 8
pages = photos // per_page
if photos % per_page != 0:
    pages += 1
print("Чтобы вклеить все фото, нужно", pages, "страниц.\n")


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
print("=== Task 10 ===")
distance = 1600
fuel_per_100 = 9
tank = 48

fuel_needed = distance / 100 * fuel_per_100
print("Для поездки нужно", fuel_needed, "литров бензина")
import math
refuels = math.ceil(fuel_needed / tank)
print("Минимум нужно заехать на заправку", refuels, "раза")