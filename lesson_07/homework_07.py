# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def add_two_numbers(a: float, b: float) -> float:
    return a + b


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(numbers: list[float]) -> float:
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(text):
    return text[::-1]


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def longest_word(words):
    if not words:
        return ""
    return max(words, key=len)


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1


# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7
"""
    Вычисляет общее количество деревьев в саду (form homework_01)

    Есть сад с яблонями, грушами и сливами:
    - груш на pears_more больше, чем яблонь
    - слив на plums_less меньше, чем яблонь
"""

def total_trees(apple_trees, pears_more, plums_less):
    pear_trees = apple_trees + pears_more
    plum_trees = apple_trees - plums_less
    total = apple_trees + pear_trees + plum_trees
    return total


# task 8
"""
    Вычисляет температуру вечером по изменениям в течение дня (form homework_01)

    Пример:
    Было start_temp градусов
    После обеда похолодало на drop градусов
    Затем потеплело на rise градусов
"""

def evening_temperature(start_temp, drop, rise):
    temp = start_temp
    temp -= drop
    temp += rise
    return temp


# task 9
"""
    Вычисляет сколько детей пришло сегодня в театра кружок

    Например:
    - в кружке boys_total мальчиков
    - девочек в girls_times_less раз меньше
    - sick_boys мальчиков сегодня не пришли
    - absent_girls девочек сегодня не пришли
"""

def children_in_theatre_group(boys_total, girls_times_less, sick_boys, absent_girls):
    girls_total = boys_total // girls_times_less
    boys_today = boys_total - sick_boys
    girls_today = girls_total - absent_girls
    return boys_today + girls_today


# task 10
"""
    Вычисляет общую стоимость трех книг

    Первая книга имеет цену first_price
    Вторая дороже первой на second_more
    Третья стоит долю от суммы первой и второй (third_share_of_sum)
"""

def total_books_price(first_price, second_more, third_share_of_sum):
    second_price = first_price + second_more
    third_price = (first_price + second_price) * third_share_of_sum
    total = first_price + second_price + third_price
    return total