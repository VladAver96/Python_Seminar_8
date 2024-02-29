from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))

    while var != 1 and command != 2:
        print("Неправильный ввод")
        var = int(input('Введите число '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")


def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range (len (data_first)):
            if data_first [i] == '\n' or i ==  len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(' '.join(data_first_list))


    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)

def update_data():
    search_query = input("Введите имя или фамилию для поиска: ")
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()

    found_indexes = []
    for i, line in enumerate(data_first + data_second):
        if search_query.lower() in line.lower():
            found_indexes.append(i)

    if not found_indexes:
        print("Запись не найдена.")
        return

    print("Найдены следующие записи:")
    for i in found_indexes:
        print(f"№{i+1}: {data_first[i] if i < len(data_first) else data_second[i - len(data_first)]}")

    choice = input("Выберите номер записи для редактирования: ")
    if not choice.isdigit() or int(choice) not in range(1, len(found_indexes) + 1):
        print("Неправильный ввод.")
        return

    index_to_edit = found_indexes[int(choice) - 1]
    new_data = input("Введите новые данные для этой записи: ")
    if index_to_edit < len(data_first):
        data_first[index_to_edit] = new_data + '\n'
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            f.writelines(data_first)
    else:
        data_second[index_to_edit - len(data_first)] = new_data + '\n'
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            f.writelines(data_second)

    print("Данные успешно обновлены.")


def delete_data():
    search_query = input("Введите имя или фамилию для поиска: ")
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()

    found_indexes = []
    for i, line in enumerate(data_first + data_second):
        if search_query.lower() in line.lower():
            found_indexes.append(i)

    if not found_indexes:
        print("Запись не найдена.")
        return

    print("Найдены следующие записи:")
    for i in found_indexes:
        print(f"№{i+1}: {data_first[i] if i < len(data_first) else data_second[i - len(data_first)]}")

    choice = input("Выберите номер записи для удаления: ")
    if not choice.isdigit() or int(choice) not in range(1, len(found_indexes) + 1):
        print("Неправильный ввод.")
        return

    index_to_delete = found_indexes[int(choice) - 1]
    if index_to_delete < len(data_first):
        data_first.pop(index_to_delete)
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            f.writelines(data_first)
    else:
        data_second.pop(index_to_delete - len(data_first))
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            f.writelines(data_second)

    print("Запись успешно удалена.")

