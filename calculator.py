while True:
    print("=== Простой калькулятор ===")
    try:
        # Необходимо ввести данные:
        x1 = float(input("Первое число: "))
        x2 = float(input("Второе число: "))
        
        # Необходимо выбрать операцию:
        operation = input("Операция (+, -, *, /): ")
        
        # Выполнение операции
        if operation == "+":
            result = x1 + x2
        elif operation == "-":
            result = x1 - x2
        elif operation == "*":
            result = x1 * x2
        elif operation == "/":
            if x2 == 0:
                print("Ошибка: на 0 делить нельзя!")
                continue
            result = x1 / x2
        else:
            print("Ошибка: неверная операция!")
            continue
        
        # Вывод результата
        print(f"Результат: {result}")
    
    except ValueError:
        print("Ошибка: введите корректное число!")
        continue
    
    # Завершение программы
    user_input = input("Нажмите Y или y для завершения программы: ")
    if user_input.lower() == "y":
        break

print("Завершение программы")