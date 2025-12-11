while True:
    word = input("Введите слово, в котором есть буква 'h': ")

    if "h" in word.lower():
        print("Все правильно")
        break
    else:
        print("В этом слове нет буквы 'h'")