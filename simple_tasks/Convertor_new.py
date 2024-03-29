print("Данный конвертор переводит заданные единицы измерения в СИ. Приступим!")
# Функция "main" создана для возможности возврата в начало программы
def main():
    while True:  # Выбор физической величины и проверка на валидность введенного значения
        quantity = int(input("Выберите физ. величину:"
                             "\n 1. Время  \n 2. Масса \n 3. Температура \n"))
        if quantity == 1 or quantity == 2 or quantity == 3:
            break
        else:
            print("Введите номер физической величины из предложенного списка!")
            continue
    # Перевод времени в секунды
    if quantity == 1:
        while True:  # Проверка на валидность введенной операции
            time_type = int(input("Тип операции:"
                                  "\n 1. дни -> сек \n 2. часы -> сек \n 3. минуты -> сек \n"))
            if time_type == 1 or time_type == 2 or time_type == 3:
                break
            else:
                print("Введите тип операции из предложенного списка!")
                continue
        time = float(input("Введите исходное значение времени: \n"))  # Ввод значения температуры
        if time_type == 1:
            print("Время в секундах: ", time * 86400)
        elif time_type == 2:
            print("Время в секундах: ", time * 60 * 60)
        elif time_type == 3:
            print("Время в секундах: ", time * 60)
    # Перевод массы в килограммы
    elif quantity == 2:
        while True:  # Проверка на валидность введенной операции
            weight_type = int(input("Тип операции: "
                                    "\n 1. Т -> Кг \n 2. Ц -> Кг \n 3. Г -> Кг \n"))
            if weight_type == 1 or weight_type == 2 or weight_type == 3:
                break
            else:
                print("Введите тип операции из предложенного списка!")
                continue
        weight = float(input("Введите исходное значение массы: \n"))  # Ввод значения массы
        if weight_type == 1:
            print("Масса в килограммах: ", weight * 1000)
        elif weight_type == 2:
            print("Масса в килограммах: ", weight * 100)
        elif weight_type == 3:
            print("Масса в килограммах: ", weight / 1000)
    # Перевод температуры в градусы Цельсия или Кельвина
    elif quantity == 3:
        while True:  # Проверка на валидность введенной операции
            temp_type = int(input("Тип операции:"
                                  "\n 1. Ф -> Ц"
                                  "\n 2. Ф-> К \n 3. Ц -> К "
                                  "\n 4. К -> Ц \n"))
            if temp_type == 1 or temp_type == 2 or temp_type == 3 or temp_type == 4:
                break
            else:
                print("Введите тип операции из предложенного списка!")
                continue
        temp = float(input("Введите исходное значение температуры: \n"))  # Ввод значения температуры
        if temp_type == 1:
            print("Температура по Цельсия: ", (temp - 32) * 5 / 9)
        elif temp_type == 2:
            print("Температура по Кельвину: ", ((temp - 32) * 5 / 9) + 273.15)
        elif temp_type == 3:
            print("Температура по Кельвину: ", temp + 273.15)
        elif temp_type == 4:
            print("Температура по Цельсия: ", temp - 273.15)
    while True:  # Запрос на запуск всей программы заново и проверка введенного ответа на валидность
        restart = int(input("Хотите начать сначала? \n"
                            "1 : Да \n"
                            "2 : Нет \n"))
        if restart == 1:
            main()
        else:
            print("Программа закончена. Пока!")
            exit()


main()  # Код начинается отсюда
