from config import BASE_DIR
from file_manager import FileManager


def show_menu():
    print("\n========== ФАЙЛОВЫЙ МЕНЕДЖЕР ==========")
    print("1. Показать текущую директорию")
    print("2. Показать содержимое директории")
    print("3. Перейти в папку")
    print("4. Создать папку")
    print("5. Удалить папку")
    print("6. Создать файл")
    print("7. Прочитать файл")
    print("8. Записать текст в файл")
    print("9. Скопировать файл")
    print("10. Переместить файл или папку")
    print("11. Переименовать файл или папку")
    print("0. Выход")


def main():
    manager = FileManager(BASE_DIR)

    while True:
        show_menu()
        command = input("Выберите команду: ")

        if command == "1":
            manager.show_current_dir()

        elif command == "2":
            manager.list_dir()

        elif command == "3":
            folder_name = input("Введите имя папки или .. для возврата назад: ")
            manager.change_dir(folder_name)

        elif command == "4":
            folder_name = input("Введите имя новой папки: ")
            manager.create_dir(folder_name)

        elif command == "5":
            folder_name = input("Введите имя папки для удаления: ")
            manager.delete_dir(folder_name)

        elif command == "6":
            file_name = input("Введите имя файла: ")
            manager.create_file(file_name)

        elif command == "7":
            file_name = input("Введите имя файла для чтения: ")
            manager.read_file(file_name)

        elif command == "8":
            file_name = input("Введите имя файла для записи: ")
            text = input("Введите текст: ")
            manager.write_file(file_name, text)

        elif command == "9":
            source_name = input("Введите имя исходного файла: ")
            destination_name = input("Введите имя нового файла: ")
            manager.copy_file(source_name, destination_name)

        elif command == "10":
            source_name = input("Введите имя исходного файла или папки: ")
            destination_name = input("Введите новое расположение или имя: ")
            manager.move_file(source_name, destination_name)

        elif command == "11":
            old_name = input("Введите старое имя: ")
            new_name = input("Введите новое имя: ")
            manager.rename_file(old_name, new_name)

        elif command == "0":
            print("Выход из программы")
            break

        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    main()