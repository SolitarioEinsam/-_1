import os 
#ввод функции очистки терминала
clear = lambda: os.system('cls')

#функция добавления нового абонента в справочник
def data_add():
    surname = input('Введите фамилию: ')
    clear()
    name = input('Введите имя: ')
    clear()
    last_surname = input('Введите фамилию: ')
    clear()
    number = input('Введите номер телефона: ')
    clear()
    with open('data.txt', 'a') as file:
        file.write(f"{line_count} {surname} {name} {last_surname} {number}\n")        

#функция поиска абонента по определенному параметру
def data_found():
    index_found = input("Введите параметр поиска: ")
    clear()
    with open('data.txt', 'r') as file:
        data_list = file.readlines()
        for line in data_list:
            if index_found in line:
                print(line)
    a = input('нажмите enter для продолжения...')
    clear()

#функция вывода всей телефонной книги в консоль
def data_output():
    with open('data.txt', 'r') as file:
        data = file.readlines()
    print(*data)
    a = input('Нажмите enter для продолжения...')
    clear()
#функция очистки базы данных
def data_clear():
    with open('data.txt', 'w'):
        a = input('Список успешно очищен, нажмите enter для продолжения...')
        clear()
    return()

#функция переноса абонента в доп базу
def data_transfer_dop_data():
    with open('data.txt', 'r') as file:
        data = file.readlines()
    print(*data)
    index_transfer = input('Введите номер абонента для переноса: ')
    clear()
    line_list_transfer = ''
    with open('data.txt', '+r') as file:
        list_line = file.readlines()
        #print(list_line)
        #print(list_line)
        for line in list_line:
            #print(line[0])
            #print(line)
            if line[0] == index_transfer:
                line_list_transfer = line
                #print(line)
                with open('dop_data.txt', 'a') as file_dop:
                    file_dop.write(line)
def data_transfer_dop_data_output():
    with open('dop_data.txt', 'r') as file:
        data = file.readlines()
    print(*data)
    a = input('Нажмите enter для продолжения...')
    clear()

index_check = False #условие выхода из основного цикла меню
#индексы для нумерации абонентов
line_count = 0
with open('data.txt', 'r') as file:
    line_count = sum(1 for line in file)
#цикл главного меню 
while index_check == False:
    print("""
    1 - добавить информацию
    2 - найти по поределенному параметру
    3 - вывести весь справочник в терминал
    4 - очистить справочник
    5 - перенести абонента в dop_data
    6 - вывод дополнительной базы абонентов
    7 - выключить справочник\n""")

    index = input('Введите цифру для выбора функции: ')
    clear()
    line_count = 1
    with open('data.txt', 'r') as file:
        line_count = sum(1 for line in file) + 1

    if index == '1':
        data_add()
    if index == '2':
        data_found()
    if index == '3':
        data_output()
    if index == '4':
        data_clear()
    if index == '5':
        data_transfer_dop_data()
    if index == '6':
        data_transfer_dop_data_output()
    if index == '7':
        index_check = True