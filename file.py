def main():
    cycle = True
    while cycle:
        print("\n")
        print("выберите действие(введите номер пункта):\n"
            "1) добавить контакт\n"
            "2) найти контакт по номреру телефона\n"
            "3) изменить контакт\n"
            "4) удалить контакт\n"
            "5) завершить работу")
        ans = int(input())
        match ans:
            case 1:
                write_data()
            case 2:
                find_data()
            case 3:
                change_data()
            case 4:
                delete_data()
            case 5:
                cycle = False

def WritePerson(second_name, first_name, phone):
    with open("file.txt", "a") as f:
        f.write(f"{second_name}, {first_name}, {phone}\n")


def write_data():
    second_name = input('введите фамилию: ')    
    first_name = input('введите имя: ') 
    phone = input('введите номер телефона: ')

    with open("file.txt", "r") as f:
        data = f.read()
        if phone in data:
            print("\n***контакт с таким номером уже существует***")
        else:
            WritePerson(second_name, first_name, phone)

def find_data():

    data = open('file.txt', 'r')
    data_lines = data.readlines()
    search = input("поиск(введите любые данные): ")
    for i in data_lines:
        if search in i:
            print(i) 
            break
    else:
        print("\n***контакт не найден***")          
    data.close()


def change_data():      # при изменение контакта будет запрашиватся номер, так как номер является уникальным данным
    number = input("введитте телефон контакта, которого хотите изменить: ")
    line = ""
    b_condition = False             
    with open("file.txt", 'r') as f:
        lines = f.readlines()

        for i in lines:
            list1 = list(i.split())
            try:
                if int(number) == int(list1[-1]):
                    line = i
                    b_condition = True
                    break
            except ValueError:
                print("\n***вы ввели не коректное значение***")
                break
        else:
            print("\n***контакта с данным номером не существует***")
                
    if b_condition:
        with open("file.txt", 'r') as f:
            old_data = f.read()

        new_second_name = input("введите фамилию: ")
        new_first_name = input("введите имя: ")
        new_phone = input("введите телефон: ")
        if new_phone in old_data:
            print("\n***контакт с таким номером уже существует***")
            b_condition = False
        else:    
            new_data = old_data.replace(line, f"{new_second_name}, {new_first_name}, {new_phone}\n")   # замена линии с указанным номером на новую информацию

            with open ('file.txt', 'w') as f:
                f.write(new_data)            


def delete_data():      # эта функция также будет хапрашивать номер телефона 
    number = input("введитте телефон контакта, которого хотите удалить: ")
    line = ""
    b_condition = False             
    with open("file.txt", 'r') as f:
        lines = f.readlines()
        for i in lines:
            list1 = list(i.split())
            try:
                if int(number) == int(list1[-1]):
                    line = i
                    b_condition = True
                    break

            except ValueError:
                print("\n***вы ввели не коректное значение***")
                break
        else:
            print("\n***контакта с данным номером не существует***")

    if b_condition:
        with open("file.txt", 'r') as f:
            old_data = f.read()

            new_data = old_data.replace(line, " ")   # замена линии с указанным номером на новую информацию

            with open ('file.txt', 'w') as f:
                f.write(new_data)  
                
main()