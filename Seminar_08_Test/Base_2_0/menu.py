def show_menu():
    print("\n" + "=" * 40)
    print("1. Показать базу")  
    print("2. Найти студента")  
    print("4. Сделать выборку по стипендиям")  
    print("5. Добавить студента")
    print("6. Отчислить студента")  
    print("7. Обновить данные студента")
    print("8. Экспортировать данные в формате json") 
    print("9. Экспортировать данные в формате xlsx") 
    print("10. Закончить работу")  
    return int(input("Введите номер необходимого действия: "))